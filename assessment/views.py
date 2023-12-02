from django.shortcuts import render, redirect
from django.urls import reverse

from asgiref.sync import sync_to_async
from .forms import AssessmentForm
import ast
import asyncio
import os
import requests
import vt

api_key = os.getenv('VIRUSTOTAL_API_KEY')
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

            result = loop.run_until_complete(main(
                selected_option, input_data
            ))

            if result:
                score = calculate_reputation_score(result)
                advice = interpret_reputation_score(score)

            return redirect(
                reverse('risk-results') +
                f'?result={result}&score={score}&advice={advice}'
            )
    else:
        form = AssessmentForm()

    return render(request, 'assessment/form.html', {'form': form})


def risk_results_view(request):
    """
    Presents the outcome of the assessment scans
    """
    result_str = request.GET.get('result', None)
    score = request.GET.get('score', None)
    advice = request.GET.get('advice', None)

    try:
        result = ast.literal_eval(result_str)
    except Exception:
        print(f'Error evaluating the string: {result_str}')
        result = None
    return render(
        request,
        'assessment/results.html',
        {'result': result, 'score': score, 'advice': advice}
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

            if file_stats:
                return file_stats
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
            if result:
                return result
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
    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip_addr}'
    headers = {
        'accept': 'application/json',
        'x-apikey': api_key,
    }
    try:
        res = requests.get(url, headers=headers)
        ip = res.json()
        result = ip['data']['attributes']['last_analysis_stats']
        if result:
            return result
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None


def calculate_reputation_score(stats):
    """
    Calculate the reputations score for a scanned item
    """
    weights = {
        'harmless': 1,
        'malicious': 3,
        'suspicious': 2,
    }

    total_score = sum(
        weights.get(category, 0) * count for category,
        count in stats.items()
    )

    max_score = sum(weights.values())
    percentage_score = (total_score // max_score) * 100

    return percentage_score


def interpret_reputation_score(score):
    """
    Defien threshold for interpretation of reputation scores
    """
    if score >= 75:
        return f'Score: {score} Resource is safe to use'
    elif 50 <= score < 75:
        return f'Score: {score} Proceed with caution'
    else:
        return f'Score: {score} Use at your own risk'


async def main(selected_option, input_data):
    """
    Async function handler
    """
    if selected_option == 'file':
        return await scan_file(input_data)
    elif selected_option == 'url':
        return await scan_url(input_data)
    elif selected_option == 'ip':
        return await sync_to_async(scan_ip)(input_data)
