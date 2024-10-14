from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request, *args, **kwargs):
    #to use for authentication later
    print(request.user)
    return HttpResponse("<h1>Index Page<h1>")

def form_view(request, *args, **kwargs):
    form_context = {
        "usn": "1BM16CS005",
        "elective_options": [
            ["COMPOSITE MATERIALS               ",'11CH7IECP1'],
            ["ADVANCED BIOPROCESS ENGINEERING   ",'11CH7IECP2'],
            ['DATA STRUCTURE                    ','11CI8IEDSN'],
            ['JAVA PROGRAMMING                  ','11CI7IEJAP'],
            ['ELECTRICAL POWER & ENERGY MGMT SYS','11EE7IE1EM'],
            ['MICRO & SMART SYSTEMS             ','11EE7IE1MS'],
            ['FINITE ELEMENT ANALYSIS           ','11ME7IEFEA'],
            ['MECHATRONICS                      ','11ME7IEMCT'],
            ['RAPID PROTOTYPING                 ','11ME7IERPT'],
            ['OPERATION RESEARCH                ','11ME7IEOPR'],
            ['GRAPH THEORY                      ','11MA7IEGRT'],
            ['NUMBER THEORY                     ','11MA7IENUT'],
            ['SATELLITE COMMUNICATION           ','12TC7IESAT'],
            ['REMOTE SENSING & GEOGRAPHICAL INFO SYS','11CV7IERSG'],
            ['BASIC FRACTURE MECHANICS          ','11CV7IEBFM'],
            ['DATA BASE MANAGEMENT SYSTEMS      ','11IM7IEDBM'],
            ['TOTAL QUALITY MANAGEMENT          ','11IM7IETQM'],
            ['FUNDAMENTALS OF MOBILE COMM       ','11EC7IE1MC'],
            ['NEURAL NETWORKS                   ','11ML7IE1NN'],
        ]
    }
    return render(request, "form.html", form_context)