from django.shortcuts import render
from .models import PythonCode
# Create your views here.
def index(request):
    return(render(request,'index.html'))

def compiler_python(request):
    if request.method == 'POST':
        form_data=request.POST
        code=form_data['code']
        #PythonCode.objects.create(code=code)
        try:
            
            output=exec(code)
        except Exception as e:
            output=str(e)
        return render(request,'result.html',{'output':output})
    return render(request,'form.html')