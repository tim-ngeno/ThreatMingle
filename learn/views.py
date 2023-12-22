from django.shortcuts import render

# Create your views here.


def learning_view(request):
    """
    Renders a template for the learning content model
    """
    data = [
        {
            'title': 'Introduction to Cybersecurity',
            'content': 'This module provides an introduction to the \
            field of cybersecurity, covering its importance, key \
            concepts, and fundamental principles.',
        },
        {
            'title': 'Network Security Basics',
            'content': 'Explore the foundations of network security, including concepts like firewalls, VPNs, and secure communication protocols.',
        },
        {
            'title': 'Web Application Security',
            'content': 'Learn about common web application security vulnerabilities and best practices for securing web applications against attacks.',
        },
        {
            'title': 'Cryptography Essentials',
            'content': 'An overview of cryptographic techniques and their applications in securing information and communication.',
        },
        {
            'title': 'Malware Analysis Techniques',
            'content': 'Dive into the world of malware analysis, understanding different types of malware and techniques for analyzing malicious code.',
        },
        {
            'title': 'Incident Response Strategies',
            'content': 'Explore strategies and best practices for incident response, including detection, analysis, containment, eradication, and recovery.',
        },
        {
            'title': 'Cloud Security Fundamentals',
            'content': 'Understand the unique challenges and solutions related to securing cloud environments, covering cloud architecture, identity management, and data protection.',
        },
        {
            'title': 'Security Awareness Training',
            'content': 'Develop an understanding of the human element in cybersecurity, focusing on security awareness training and promoting a security-conscious culture.',
        },
        {
            'title': 'Mobile Security Principles',
            'content': 'Examine security principles and challenges associated with mobile devices, mobile applications, and the protection of sensitive data on mobile platforms.',
        },
        {
            'title': 'IoT Security Considerations',
            'content': 'Investigate security considerations and best practices for securing Internet of Things (IoT) devices and ecosystems.',
        },
    ]

    return render(request, 'learn/index.html', {'data': data})
