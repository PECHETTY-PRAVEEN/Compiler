from django.shortcuts import render
from sqlalchemy import null
from .models import PythonCode
import subprocess as sb
# Create your views here.
def index(request):
    return(render(request,'index.html'))

def compiler_python(request):
    if request.method == 'POST':
        form_data=request.POST
        code=form_data['code']
        #PythonCode.objects.create(code=code)
        
        try:
            f = open("code.py", "w")
            f.write(code)
            f.close()
            #exec('python code.py')
            output= sb.getoutput('python code.py')
        except Exception as e:
            output=str(e)
        return render(request,'form.html',{'output':output,'code':code})
    return render(request,'form.html')