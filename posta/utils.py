from datetime import datetime

from django.shortcuts import redirect

from anagrafica.models import Persona


def imposta_destinatari_e_scrivi_messaggio(request, qs_destinatari=Persona.objects.none()):
    request.session["messaggio_destinatari"] = qs_destinatari
    request.session["messaggio_destinatari_timestamp"] = datetime.now()
    return redirect("/posta/scrivi/")
