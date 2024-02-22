from django import forms
from django.shortcuts import render
from django.views.generic import View
from math import pow


# Create your views here.

# class Addition(View):
#     def get(self,request):

#         return render(request,"hello.html")
    
# class Greet(View):
#     def get(self,request):
#         return render(request,"hello.html")
    
#     def post(self,request):
#         print(request.POST)

#         return render(request,"hello.html")

class Addition(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addition.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        res=int(n1)+int(n2)
        print(res)
        return render(request,"addition.html",{"result":res})
    
class Subtraction(View):
    def get(self,request,*args,**kwargs):
        return render(request,"subtraction.html")
   
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        res=int(n1)-int(n2)
        print(res)
        return render(request,"subtraction.html",{"result":res})
    
class Division(View):
    def get(self,request,*args,**kwargs):
        return render(request,"division.html")

    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        res=int(n1)/int(n2)
        print(res)
        return render(request,"division.html",{"result":res})   

class Product(View):
    def get(self,request,*args,**kwargs):
        return render(request,"product.html")  
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        res=int(n1)*int(n2)
        print(res)
        return render(request,"product.html",{"result":res})
    
class Cube(View):
    def get(self,request,*args,**kwargs):
        return render(request,"cube.html") 
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        res=int(n1)*int(n1)*int(n1)      
        print(res)
        return render(request,"cube.html",{"result":res})
    
class PrimeNumber(View):
    def get(self,request,*args,**kwargs):
        return render(request,"primenumber.html") 
    
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        
        
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    result="not prime"
                else:
                    result="prime number"
        
        return render(request,"primenumber.html",{"result":result})
    
class LeapYear(View):
    def get(self,request,*args,**kwargs):
        return render(request,"leapyear.html") 
    

    def post(self,request,*args,**kwargs):
        year=int(request.POST.get("year"))
        if year%100==0 and year%400==0 or year%100!=0 and year %4==0:
            result="leap year"
        else:
            result="not leap year"
        return render(request,"leapyear.html",{"result":result})
    
class LongestWordView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"longestword.html")
    
    def post(self,request,*args,**kwargs):
        words=request.POST.get("words").split(" ")
        result=max(words,key=lambda w:len(w))
        return render(request,"longestword.html",{"result":result})
    
class BracketView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"brackets.html")
    def post(self,request,*args,**kwargs):
        bracket=request.POST.get("bracket")
        if bracket==({[]}):
            result="valid"
        else:
            result="invalid"
        
        return render(request,"brackets.html",{"result":result})
    
class MostFrequentWord(View):
    def get(self,request,*args,**kwargs):
        return render(request,"frequent.html")
    
    def post(self,request,*args,**kwargs):
        word=request.POST.get("word")
        wc={}
        for w in word:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
            print(wc)

            return render(request,"frequent.html",{"result":wc})

class EmiForm(forms.Form):
    Loan_amount=forms.CharField()
    Tenure=forms.IntegerField()
    intrest=forms.IntegerField()



class LoanView(View):
    def get(self,request,*args,**kwargs):
        form=EmiForm()
        return render(request,"emi.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=EmiForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            principal=form.cleaned_data.get("Loan_amount")
            tenure=form.cleaned_data.get("Tenure")
            roi=form.cleaned_data.get("interest")
            n=tenure*12
            monthly_interest_rate=(roi/100)/12
            emi=(principal*monthly_interest_rate*pow(1+monthly_interest_rate,n))/(pow(1+monthly_interest_rate,n)-1)
            print(emi)
        else:
            print("error")
        return render(request,"emi.html",{"form":form})    