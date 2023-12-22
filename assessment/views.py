from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from asgiref.sync import sync_to_async
from .forms import AssessmentForm
from decouple import config
import ast
import asyncio
import ipaddress
import re
import requests
import vt

api_key = config('VIRUSTOTAL_API_KEY')
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def risk_assessment_view(request):
    """
    Renders a personalized risk assessment page
    """
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['options']
            input_data = form.cleaned_data['input_data']

            result, score = loop.run_until_complete(main(
                selected_option, input_data
            ))

            if result:
                print(result, '\n', score)
                score = score // 100 if score > 100 else score
                return redirect(
                    reverse('risk-results') +
                    f'?result={result}&score={score}'
                )
            else:
                return 'Error: Failed to perform the scan'
        else:
            return 'Invalid form data'
    else:
        form = AssessmentForm()

    return render(request, 'assessment/form.html', {
        'form': form, 'title': 'Assessment'})


def risk_results_view(request):
    """
    Presents the outcome of the assessment scans
    """
    result_str = request.GET.get('result', None)
    score = request.GET.get('score', None)

    try:
        result = ast.literal_eval(result_str)
    except Exception:
        print(f'Error evaluating the string: {result_str}')
        result = None
    return render(
        request,
        'assessment/results.html',
        {
            'result': result, 'score': score, 'title': 'Result'
        }
    )


async def scan_file(file_hash):
    """
    Scans a file hash for possible threats
    """
    try:
        async with vt.Client(api_key) as client:
            file_data = await client.get_object_async(
                f'/files/{file_hash}'
            )
            file_stats = file_data.get('last_analysis_stats')
            score = file_data.get('reputation')

            if file_stats and score:
                return file_stats, score
            else:
                print(f'No stats found for file hash {file_hash}')
                return None

    except vt.APIError as e:
        print(f'VirusTotal API Error: {e}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None


async def scan_url(url_addr):
    """
    Perform a scan on URL address for potential risks
    """
    try:
        async with vt.Client(api_key) as client:
            url_id = vt.url_id(url_addr)
            url = await client.get_object_async(
                f'/urls/{url_id}'
            )
            result = url.get('last_analysis_stats')
            score = url.get('reputation')

            if result:
                return result, score
            else:
                return None
    except vt.APIError as e:
        print(f'VirusTotal API error: {e}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None


def scan_ip(ip_addr):
    """
    Scan IP address for potential risks
    """
    if is_valid_ip(ip_addr):
        url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip_addr}'
        headers = {
            'accept': 'application/json',
            'x-apikey': api_key,
        }
        try:
            res = requests.get(url, headers=headers)
            ip = res.json()
            result = ip['data']['attributes']['last_analysis_stats']
            score = ip['data']['attributes']['reputation']
            if result:
                return result, score
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return None
    else:
        return None


def is_valid_hash(hash_value):
    """
    Checks if provided string is a valid MD5 or SHA-256 hash.
    """
    # MD5 hashes should be 32 characters long, hexadecimal characters
    md5_pattern = re.compile(r'^[0-9A-Fa-f]{32}$')

    # SHA-256 should be 64 characters long,hexadecimal characters
    sha_256_pattern = re.compile(r'^[0-9A-Fa-f]{64}$')

    return bool(md5_pattern.match(hash_value) or
                bool(sha_256_pattern.match(hash_value)))


def is_valid_ip(ip_address):
    """
    Checks if the provided string is a valid IP address
    """
    try:
        ipaddress.IPv4Address(ip_address)
        return True
    except ipaddress.AddressValueError:
        try:
            ipaddress.IPv6Address(ip_address)
            return True
        except ipaddress.AddressValueError:
            return False


async def main(selected_option, input_data):
    """
    Async function handler
    """
    if selected_option == 'file':
        if is_valid_hash(input_data):
            print("valid hash")
            return await scan_file(input_data)
        print("invalid hash")
        return HttpResponseBadRequest('Invalid input data format')
    elif selected_option == 'url':
        return await scan_url(input_data)
    elif selected_option == 'ip':
        if is_valid_ip(input_data):
            return await sync_to_async(scan_ip)(input_data)
