"""
Questo modulo e' una collezione di Tratti.

I tratti possono essere aggiunti ai modelli per aggiugere
dei set di funzionalita'. Si noti bene che ogni tratto
potrebbe necessitare l'implementazione di metodi o proprieta'
particolari. Fare riferimento alla documentazione del tratto
utilizzato.
"""
from datetime import date, datetime, timedelta
from django.apps import AppConfig, apps
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q
from anagrafica.costanti import ESTENSIONE, ESTENSIONE_MINORE
from base.utils import concept
from django.utils import timezone


class ConMarcaTemporale(models.Model):
    """
    Aggiunge le marche temporali automatiche di creazione ed ultima modifica.
    """

    class Meta:
        abstract = True

    creazione = models.DateTimeField(default=timezone.now, db_index=True)
    ultima_modifica = models.DateTimeField(auto_now=True, db_index=True)



class ConProtocollo(models.Model):
    """
    Aggiunge data e numero di protocollo.
    """

    class Meta:
        abstract = True

    protocollo_numero = models.CharField('Numero di protocollo', max_length=512, null=True)
    protocollo_data = models.DateField('Data di presa in carico', null=True)


class ConEstensione(models.Model):
    """
    Aggiunge un Sede ed un livello di estensione dell'oggetto.
    """

    class Meta:
        abstract = True

    sede = models.ForeignKey("anagrafica.Sede", db_index=True)
    estensione = models.CharField("Estensione", max_length=1, choices=ESTENSIONE, db_index=True)

    def possibili_estensioni(self, sede=None):
        """
        Dato un sede, od il sede gia' salvato, ritorna le possibili estensioni.
        :param sede: Opzionale. Il sede. Quello gia' salvato se non specificato.
        :return: (chiave, valore), (chiave, valore)
        """

        if sede is None:
            sede = self.sede

        return (
            (chiave, valore) for (chiave, valore) in ESTENSIONE
            if chiave in ESTENSIONE_MINORE[sede.estensione]
            or chiave == sede.estensione
        )


class ConStorico(models.Model):
    """
    Aggiunge un inizio, una fine ed una verifica per attualita'.
    """

    class Meta:
        abstract = True


    # Puo' essere sovrascritto per aggiungere una ulteriore
    # condizione di attualita' (es. partecipazione confermata, ecc.)
    CONDIZIONE_ATTUALE_AGGIUNTIVA = Q()

    inizio = models.DateTimeField("Inizio", db_index=True, null=False)
    fine = models.DateTimeField("Fine", db_index=True, null=True, blank=True, default=None, help_text="Lasciare il campo "
                                                                                                  "vuoto per impostare "
                                                                                                  "fine indeterminata.")

    @classmethod
    @concept
    def query_attuale(cls, al_giorno=timezone.now(), **kwargs):
        """
        Restituisce l'oggetto Q per filtrare le entita' attuali.

        NOTA BENE: https://pypi.python.org/pypi/django-conceptq/0.1.0
        :param al_giorno: Giorno per considerare la verifica per l'attuale. Default oggi.
        :return: Q!
        """

        if isinstance(al_giorno, datetime):  # Se orario esatto
            inizio = fine = al_giorno

        else:  # Altrimenti, se solo giorno
            inizio = datetime.combine(al_giorno, datetime.max.time())  # 23.59
            fine = datetime.combine(al_giorno, datetime.min.time())  # 0.00

        fine += timedelta(seconds=1)  # Anti-bug

        return Q(
            Q(inizio__lte=inizio),
            Q(Q(fine__isnull=True) | Q(fine__gt=fine)),
            cls.CONDIZIONE_ATTUALE_AGGIUNTIVA,
            **kwargs
        )

    @classmethod
    @concept
    def query_attuale_tra_date(cls, inizio, fine, **kwargs):
        """
        Restituisce l'oggetto Q per filtrare le entita' che sono state
         attuali in qualsiasi momento in un periodo compreso tra due date.

        NOTA BENE: https://pypi.python.org/pypi/django-conceptq/0.1.0
        :param inizio: Giorno di inizio (es. primo dell'anno)
        :param fine: Giorno di fine (es. ultimo dell'anno)
        :return: Q!
        """

        return Q(
            Q(Q(fine__gte=inizio) | Q(fine__isnull=True)),
            cls.CONDIZIONE_ATTUALE_AGGIUNTIVA,
            inizio__lte=fine,
            **kwargs
        )

    @classmethod
    @concept
    def query_attuale_in_anno(cls, anno, **kwargs):
        """
        Restituisce l'oggetto Q per filtrare le entita' attuali.

        NOTA BENE: https://pypi.python.org/pypi/django-conceptq/0.1.0
        :param inizio: Giorno di inizio (es. primo dell'anno)
        :param fine: Giorno di fine (es. ultimo dell'anno)
        :return: Q!
        """

        inizio = date(anno, 1, 1)
        fine = date(anno, 12, 31)

        return Q(
            Q(Q(fine__gte=inizio) | Q(fine__isnull=True)),
            cls.CONDIZIONE_ATTUALE_AGGIUNTIVA,
            inizio__lte=fine,
            **kwargs
        )

    def attuale(self, al_giorno=datetime.now()):
        """
        Controlla se l'entita' e' attuale o meno.
        :param al_giorno: Giorno per considerare la verifica per l'attuale. Default oggi.
        :return: True o False.
        """
        return self.__class__.objects.filter(self.query_attuale(al_giorno).q, pk=self.pk).exists()


class ConDelegati(models.Model):
    """
    Aggiunge la possibilita' di gestire e aggiungere delegati.
    """

    class Meta:
        abstract = True

    deleghe = GenericRelation(
        'anagrafica.Delega',
        related_query_name="%(class)s",
        content_type_field='oggetto_tipo',
        object_id_field='oggetto_id'
    )

    def deleghe_attuali(self, al_giorno=datetime.today(), **kwargs):
        """
        Ottiene QuerySet per gli oggetti Delega validi ad un determinato giorno.
        :param al_giorno: Giorno da verificare. Se assente, oggi.
        :return: QuerySet di oggetti Delega.
        """
        Delega = apps.get_model(app_label='anagrafica', model_name='Delega')
        return self.deleghe.filter(Delega.query_attuale(al_giorno, **kwargs).q)

    def delegati_attuali(self, al_giorno=datetime.today(), **kwargs):
        """
        Ottiene QuerySet per gli oggetti Persona delegati ad un determinato giorno.
        :param al_giorno: Giorno da verificare. Se assente, oggi.
        :return: QuerySet di oggetti Persona.
        """
        Persona = apps.get_model(app_label='anagrafica', model_name='Persona')
        return Persona.objects.filter(delega__in=self.deleghe_attuali(al_giorno, **kwargs))

    def aggiungi_delegato(self, tipo, persona, firmatario=None, inizio=timezone.now(), fine=None):
        """
        Aggiunge un delegato per l'oggetto. Nel caso in cui una nuova delega (attuale)
         viene inserita, contemporaneamente ad una delega attuale per la stessa persona,
         sempre attuale, questa ultima viene estesa. Assicura quindi l'assenza di duplicati.
        :param tipo: Tipologia di delega.
        :param persona: La Persona da delegare al trattamento dell'oggetto.
        :param firmatario: Persona che inserisce la delega, opzionale.
        :param inizio: Inizio della delega. Se non specificato, inizio immediato.
        :param fine: Fine della delega. Se non specificato o None, fine indeterminata.
        :return: Oggetto delegato inserito.
        """

        # Se il nuovo inserimento e' attuale
        if inizio <= timezone.now() and (fine is None or fine >= timezone.now()):

            # Cerca eventuali deleghe pari gia' esistenti.
            delega_pari = self.deleghe_attuali().filter(persona=persona, tipo=tipo)

            # Se esiste, estende se necessario, e ritorna la delega passata
            if delega_pari.exists():
                delega_pari = delega_pari[0]
                delega_pari.inizio = min(delega_pari.inizio, inizio)
                delega_pari.fine = None if fine is None or delega_pari.fine is None else max(delega_pari.fine, fine)
                delega_pari.save()
                return delega_pari

        # Aggiungi la nuova delega.
        Delega = apps.get_model(app_label='anagrafica', model_name='Delega')
        d = Delega(oggetto=self, persona=persona, inizio=inizio, fine=fine, tipo=tipo, firmatario=firmatario)
        d.save()
        return d

class ConPDF():

    def genera_pdf(self):
        raise NotImplemented('La classe non implementa il metodo "genera_pdf"')


    @property
    def url_pdf(self):
        content_type = ContentType.objects.get_for_model(self)
        app_label = content_type.app_label
        model = content_type.model
        pk = self.pk
        return "/pdf/%s/%s/%d/" % (
            app_label,
            model,
            pk
        )
