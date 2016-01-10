# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autoparco',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creazione', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('ultima_modifica', models.DateTimeField(auto_now=True, db_index=True)),
                ('estensione', models.CharField(max_length=1, choices=[('T', 'Unità Territoriale'), ('L', 'Sede Locale'), ('P', 'Sede Provinciale'), ('R', 'Sede Regionale'), ('N', 'Sede Nazionale')], db_index=True, verbose_name='Estensione')),
                ('sede', models.ForeignKey(to='anagrafica.Sede')),
            ],
            options={
                'verbose_name_plural': 'Autoparchi',
            },
        ),
        migrations.CreateModel(
            name='Collocazione',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('inizio', models.DateTimeField(db_index=True, verbose_name='Inizio')),
                ('fine', models.DateTimeField(default=None, blank=True, help_text='Lasciare il campo vuoto per impostare fine indeterminata.', null=True, verbose_name='Fine', db_index=True)),
                ('autoparco', models.ForeignKey(to='veicoli.Autoparco', related_name='autoparco')),
            ],
            options={
                'verbose_name_plural': 'Collocazioni veicolo',
                'verbose_name': 'Collocazione veicolo',
            },
        ),
        migrations.CreateModel(
            name='FermoTecnico',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creazione', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('ultima_modifica', models.DateTimeField(auto_now=True, db_index=True)),
                ('inizio', models.DateTimeField(db_index=True, verbose_name='Inizio')),
                ('fine', models.DateTimeField(default=None, blank=True, help_text='Lasciare il campo vuoto per impostare fine indeterminata.', null=True, verbose_name='Fine', db_index=True)),
            ],
            options={
                'verbose_name_plural': 'Fermi tecnici',
                'verbose_name': 'Fermo tecnico',
            },
        ),
        migrations.CreateModel(
            name='Immatricolazione',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creazione', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('ultima_modifica', models.DateTimeField(auto_now=True, db_index=True)),
                ('richiedente', models.ForeignKey(to='anagrafica.Sede', related_name='immatricolazioni_richieste')),
                ('ufficio', models.ForeignKey(to='anagrafica.Sede', related_name='immatricolazioni_istruite')),
            ],
            options={
                'verbose_name_plural': 'Pratiche di Immatricolazione',
                'verbose_name': 'Pratica di Immatricolazione',
            },
        ),
        migrations.CreateModel(
            name='Manutenzione',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creazione', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('ultima_modifica', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'verbose_name_plural': 'Interventi di Manutenzione',
                'verbose_name': 'Intervento di Manutenzione',
            },
        ),
        migrations.CreateModel(
            name='Rifornimento',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creazione', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('ultima_modifica', models.DateTimeField(auto_now=True, db_index=True)),
                ('numero', models.PositiveIntegerField(default=1, db_index=True, verbose_name='Num. rifornimento')),
                ('data', models.DateTimeField(db_index=True, verbose_name='Data rifornimento')),
                ('contachilometri', models.PositiveIntegerField(db_index=True, verbose_name='Contachilometri')),
                ('consumo_carburante', models.FloatField(default=None, blank=True, null=True, db_index=True, verbose_name='Consumo carburante lt.')),
                ('consumo_olio_m', models.FloatField(default=None, blank=True, null=True, db_index=True, verbose_name='Consumo Olio motori Kg.')),
                ('consumo_olio_t', models.FloatField(default=None, blank=True, null=True, db_index=True, verbose_name='Consumo Olio trasmissioni Kg.')),
                ('consumo_olio_i', models.FloatField(default=None, blank=True, null=True, db_index=True, verbose_name='Consumo Olio idraulico Kg.')),
                ('presso', models.CharField(max_length=1, default='D', choices=[('I', 'Cisterna interna'), ('C', 'Distributore convenzionato'), ('D', 'Distributore occasionale')], verbose_name='Presso')),
                ('contalitri', models.FloatField(default=None, blank=True, null=True, db_index=True, verbose_name='(c/o Cisterna int.) Contalitri')),
                ('ricevuta', models.CharField(max_length=32, default=None, null=True, verbose_name='(c/o Distributore) N. Ricevuta', db_index=True, blank=True)),
                ('conducente', models.ForeignKey(to='anagrafica.Persona', related_name='rifornimenti')),
            ],
            options={
                'verbose_name_plural': 'Rifornimenti di carburante',
                'verbose_name': 'Rifornimento di carburante',
            },
        ),
        migrations.CreateModel(
            name='Segnalazione',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creazione', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('ultima_modifica', models.DateTimeField(auto_now=True, db_index=True)),
                ('descrizione', models.TextField(max_length=1024, verbose_name='Descrizione')),
                ('autore', models.ForeignKey(to='anagrafica.Persona', related_name='segnalazioni')),
                ('manutenzione', models.ForeignKey(blank=True, related_name='segnalazioni', null=True, to='veicoli.Manutenzione')),
            ],
            options={
                'verbose_name_plural': 'Segnalazioni di malfunzionamento o incidente',
                'verbose_name': 'Segnalazione di malfunzionamento o incidente',
            },
        ),
        migrations.CreateModel(
            name='Veicolo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creazione', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('ultima_modifica', models.DateTimeField(auto_now=True, db_index=True)),
                ('stato', models.CharField(max_length=2, default='OK', choices=[('IM', 'In immatricolazione'), ('OK', 'In servizio'), ('KO', 'Dismesso/Fuori uso')], verbose_name='Stato')),
                ('libretto', models.CharField(max_length=16, help_text='Formato 201X-XXXXXXXXX', db_index=True, verbose_name='N. Libretto')),
                ('targa', models.CharField(max_length=5, help_text='Targa del Veicolo, senza spazi.', db_index=True, verbose_name='Targa (A)')),
                ('formato_targa', models.CharField(max_length=1, default='A', choices=[('A', 'Targa per Autoveicoli (A)'), ('B', 'Targa per Autoveicoli (B), per alloggiamenti viconlati'), ('C', 'Targa per Motoveicoli, Veicoli Speciali, Macchine Operatrici'), ('D', 'Targa per Rimorchi')], verbose_name='Formato Targa')),
                ('prima_immatricolazione', models.DateField(db_index=True, verbose_name='Prima Immatricolazione (B)')),
                ('proprietario_cognome', models.CharField(max_length=127, default='Croce Rossa Italiana', verbose_name='Proprietario: Cognome o Ragione Sociale (C2.1)')),
                ('proprietario_nome', models.CharField(max_length=127, default='Comitato Centrale', verbose_name='Proprietario: Nome o Iniziale (C2.2)')),
                ('proprietario_indirizzo', models.CharField(max_length=127, default='Via Toscana, 12, 00187 Roma (RM), Italia', verbose_name='Proprietario: Indirizzo (C2.3)')),
                ('pneumatici_anteriori', models.CharField(max_length=32, help_text='es. 215/70 R12C', verbose_name='Pneumatici: Anteriori')),
                ('pneumatici_posteriori', models.CharField(max_length=32, help_text='es. 215/70 R12C', verbose_name='Pneumatici: Posteriori')),
                ('pneumatici_alt_anteriori', models.CharField(max_length=32, blank=True, help_text='es. 215/70 R12C', null=True, verbose_name='Pneumatici alternativi: Anteriori')),
                ('pneumatici_alt_posteriori', models.CharField(max_length=32, blank=True, help_text='es. 215/70 R12C', null=True, verbose_name='Pneumatici alternativi: Posteriori')),
                ('cambio', models.CharField(max_length=32, default='Meccanico', help_text='Tipologia di Cambio', verbose_name='Cambio')),
                ('lunghezza', models.FloatField(blank=True, null=True, verbose_name='Lunghezza m.')),
                ('larghezza', models.FloatField(blank=True, null=True, verbose_name='Larghezza m.')),
                ('sbalzo', models.FloatField(blank=True, null=True, verbose_name='Sbalzo m.')),
                ('tara', models.PositiveIntegerField(blank=True, null=True, verbose_name='Tara kg.')),
                ('marca', models.CharField(max_length=32, help_text='es. Fiat', verbose_name='Marca (D.1)')),
                ('modello', models.CharField(max_length=32, help_text='es. Ducato', verbose_name='Tipo (D.2)')),
                ('telaio', models.CharField(max_length=24, help_text='Numero di telaio del veicolo, es. ZXXXXXXXXXXXXXXX', db_index=True, unique=True, verbose_name='Numero Identificazione Veicolo (E)')),
                ('massa_max', models.PositiveIntegerField(verbose_name='Massa Massima a carico (F.2)')),
                ('data_immatricolazione', models.DateField(db_index=True, verbose_name='Data immatricolazione attuale (I)')),
                ('categoria', models.CharField(max_length=16, help_text='es. Ambulanza', db_index=True, verbose_name='Categoria del Veicolo (J)')),
                ('destinazione', models.CharField(max_length=32, help_text='es. Amb. Soccorso (AMB-A)', verbose_name='Destinazione ed uso (J.1)')),
                ('carrozzeria', models.CharField(max_length=16, help_text='es. Chiuso', verbose_name='Carrozzeria (J.2)')),
                ('omologazione', models.CharField(max_length=32, blank=True, help_text='es. OEXXXXXXXXXX', null=True, verbose_name='N. Omologazione (K)')),
                ('num_assi', models.PositiveSmallIntegerField(default=2, verbose_name='Num. Assi (L)')),
                ('rimorchio_frenato', models.FloatField(blank=True, null=True, verbose_name='Massa massima a Rimorchio frenato tecnicamente ammissibile (O) kg.')),
                ('cilindrata', models.PositiveIntegerField(verbose_name='Cilindrata (P.1)')),
                ('potenza_massima', models.PositiveIntegerField(verbose_name='Potenza Massima (P.2) kW.')),
                ('alimentazione', models.CharField(max_length=1, default='B', choices=[('B', 'Benzina'), ('G', 'Gasolio'), ('P', 'GPL'), ('M', 'Metano'), ('E', 'Elettrica')], verbose_name='Alimentazione (P.3)')),
                ('posti', models.SmallIntegerField(default=5, verbose_name='N. Posti a sedere conducente compreso (S.1)')),
                ('regine', models.PositiveIntegerField(verbose_name='Livello Sonoro: Regime del motore (U.2)')),
                ('card_rifornimento', models.CharField(max_length=64, blank=True, null=True, verbose_name='N. Card Rifornimento')),
                ('selettiva_radio', models.CharField(max_length=64, blank=True, null=True, verbose_name='Selettiva Radio')),
                ('telepass', models.CharField(max_length=64, blank=True, null=True, verbose_name='Numero Telepass')),
                ('intervallo_revisione', models.PositiveIntegerField(default=365, choices=[(365, '1 anno (365 giorni)'), (730, '2 anni (730 giorni)')], verbose_name='Intervallo Revisione')),
            ],
            options={
                'verbose_name_plural': 'Veicoli',
            },
        ),
        migrations.AddField(
            model_name='segnalazione',
            name='veicolo',
            field=models.ForeignKey(to='veicoli.Veicolo', related_name='segnalazioni'),
        ),
        migrations.AddField(
            model_name='rifornimento',
            name='segnalazione',
            field=models.ForeignKey(default=None, blank=True, help_text='Rapporto conducente', null=True, to='veicoli.Segnalazione'),
        ),
        migrations.AddField(
            model_name='rifornimento',
            name='veicolo',
            field=models.ForeignKey(to='veicoli.Veicolo', related_name='rifornimenti'),
        ),
        migrations.AddField(
            model_name='immatricolazione',
            name='veicolo',
            field=models.ForeignKey(to='veicoli.Veicolo', related_name='richieste_immatricolazione'),
        ),
        migrations.AddField(
            model_name='fermotecnico',
            name='veicolo',
            field=models.ForeignKey(to='veicoli.Veicolo', related_name='fermi_tecnici'),
        ),
        migrations.AddField(
            model_name='collocazione',
            name='veicolo',
            field=models.ForeignKey(to='veicoli.Veicolo', related_name='collocazioni'),
        ),
    ]
