from django.shortcuts import render

# Create your views here.


def learning_view(request):
    """
    Renders a template for the learning content model
    """
    data = [
        {
            'title': 'Intro to Cyber Security',
            'content': 'Lorem Ipsum dolor sit amet...',
        },
        {
            'title': 'Intro to Network Security',
            'content': 'Lorem Ipsum dolor sit amet...',
        },
        {
            'title': 'What is DDOS',
            'content': 'Lorem Ipsum dolor sit amet...',
        },
        {
            'title': 'Is Cyber Security really all that?',
            'content': 'Lorem Ipsum dolor sit amet...',
        },
        {
            'title': 'Keeping yourself safe from cyber threats',
            'content': 'Lorem Ipsum dolor sit amet...',
        },
    ]

    return render(request, 'learn/index.html', {'data': data})
