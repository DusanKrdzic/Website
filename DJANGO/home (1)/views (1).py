from django.shortcuts import render, redirect


from django.core.mail import send_mail


def english(request):


    if(request.method == 'POST'):

            name = request.POST['NAME']
            email = request.POST['EMAIL']
            phone = request.POST['PHONE']
            room = request.POST['ROOM']
            arrival = request.POST['ARRIVAL']
            departure = request.POST['DEPARTURE']
            note = request.POST['NOTES']
            body = {"NAME": name, "E-MAIL": email, "PHONE": phone, "ROOM": room,
                "ARRIVAL": arrival, "DEPARTURE": departure, "NOTE": note}
            # turn the dict into a set of strings
            content = {"%s: %s" % (key, value)for (key, value) in body.items()}
             # turn those strings into 1 block of text separated by newlines
            content = "\n".join(content)
            send_mail('HOTEL RESERVATION', content,
              'dukak97@gmail.com',
             ['krdzicmdusan@gmail.com', ], fail_silently=False)
            return redirect('english')
    else:
            return render(request,'english.html')






 


def deutsch(request):

 if(request.method=='POST'):
       
            
            name=request.POST['NAME']
            email=request.POST['EMAIL']
            phone=request.POST['PHONE']
            room=request.POST['ROOM']
            arrival=request.POST['ARRIVAL']
            departure=request.POST['DEPARTURE']
            note=request.POST['NOTES']
            body={"NAME":name, "E-MAIL":email, "PHONE":phone, "ROOM":room, "ARRIVAL":arrival, "DEPARTURE":departure,"NOTE":note }
            # turn the dict into a set of strings
            content = {"%s: %s" % (key, value) for (key, value) in body.items()}
             # turn those strings into 1 block of text separated by newlines
            content = "\n".join(content)
            send_mail('HOTEL RESERVATION',content,
              'dukak97@gmail.com', 
             ['krdzicmdusan@gmail.com', ], fail_silently=False)
            return redirect('deutsch')
 else:
          return render(request,'deutsch.html')




def burgaltena(request):
    return render(request, 'burgaltena.html')


def burgaltenaEN(request):
    return render(request, 'burgaltenaEN.html')
