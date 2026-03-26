"""
Simulation complète FR : ~300 emails de gestion locative professionnelle.
50 en boîte de réception (non lus), 250 archivés (lus).

Types de mails :
- Communications internes (équipe)
- Communications locataires
- Communications prestataires
- Communications propriétaires
- Admin / juridique / assurance
- Spam / newsletters

Formats :
- Emails seuls
- Emails seuls faisant référence à un thread
- Emails en thread (conversations)
- Emails avec pièces jointes simulées
"""

import random as _random

# ---------------------------------------------------------------------------
# Constantes : locataires, prestataires, équipe, propriétaires, biens
# ---------------------------------------------------------------------------

FR_TENANTS = [
    ("Marc Dupont", "m.dupont.locataire@gmail.com", "8 avenue Foch, Boulogne", "2B"),
    ("Sophie Dupont", "s.dupont.locataire@gmail.com", "8 avenue Foch, Boulogne", "2B"),
    ("Karim Benamara", "k.benamara.loc@gmail.com", "23 rue Voltaire, Lyon", "4A"),
    ("Christine Lambert", "c.lambert.appt@gmail.com", "15 rue des Lilas, Paris", "4A"),
    ("Antonio Rodriguez", "a.rodriguez.tenant@gmail.com", "5 impasse des Acacias, Toulouse", "1C"),
    ("Marie Petit", "m.petit.locataire@gmail.com", "15 rue des Lilas, Paris", "3B"),
    ("Tran Nguyen", "t.nguyen.loc@gmail.com", "23 rue Voltaire, Lyon", "2C"),
    ("Isabelle Martin", "i.martin.locataire@gmail.com", "8 avenue Foch, Boulogne", "2A"),
    ("Jean-Pierre Dubois", "jp.dubois.loc@gmail.com", "42 bd Gambetta, Bordeaux", "5B"),
    ("Catherine Moreau", "c.moreau.loc@gmail.com", "17 rue du Marché, Nantes", "1A"),
    ("François Bernard", "f.bernard.loc@gmail.com", "42 bd Gambetta, Bordeaux", "3A"),
    ("Fatima Bouzid", "f.bouzid.loc@gmail.com", "15 rue des Lilas, Paris", "1B"),
    ("Patrick Leroy", "p.leroy.locataire@gmail.com", "Rés. Les Tilleuls, Montreuil", "6C"),
    ("Amina Diallo", "a.diallo.loc@gmail.com", "Rés. Les Tilleuls, Montreuil", "3A"),
    ("Nicolas Roux", "n.roux.tenant@gmail.com", "17 rue du Marché, Nantes", "2B"),
    ("Émilie Garnier", "e.garnier.loc@gmail.com", "Rés. Le Clos Fleuri, Bordeaux", "4D"),
    ("Youssef El Amrani", "y.elamrani.loc@gmail.com", "5 impasse des Acacias, Toulouse", "3B"),
    ("Hélène Fournier", "h.fournier.loc@gmail.com", "Rés. Le Clos Fleuri, Bordeaux", "2A"),
    ("Olivier Mercier", "o.mercier.loc@gmail.com", "Rés. Les Tilleuls, Montreuil", "5B"),
    ("Nathalie Simon", "n.simon.loc@gmail.com", "23 rue Voltaire, Lyon", "1A"),
]

FR_CONTRACTORS = [
    ("Duplex Plomberie", "contact@duplex-plomberie.fr", "Plombier"),
    ("ThermoConfort SARL", "devis@thermoconfort.fr", "Chauffagiste"),
    ("Azur Ascenseurs", "service@azur-ascenseurs.fr", "Ascensoriste"),
    ("ProNet Services", "commercial@pronet-services.fr", "Nettoyage"),
    ("Serrures Express", "contact@serrures-express.fr", "Serrurier"),
    ("Elec+ Électricité", "devis@elecplus.fr", "Électricien"),
    ("Toitures Durand", "contact@toitures-durand.fr", "Couvreur"),
    ("SOS Nuisibles", "intervention@sos-nuisibles.fr", "Désinsectisation"),
    ("Peinture & Ravalement Girard", "devis@girard-ravalement.fr", "Ravalement"),
    ("Menuiserie Caron", "atelier@menuiserie-caron.fr", "Menuisier"),
    ("ABC Diagnostics", "rdv@abc-diagnostics.fr", "Diagnostiqueur"),
    ("Jardins Méditerranée", "contact@jardins-med.fr", "Paysagiste"),
]

FR_INTERNAL = [
    ("Sophie Marchand", "s.marchand@elron-gestion.fr", "Directrice d'agence"),
    ("Thomas Lefèvre", "t.lefevre@elron-gestion.fr", "Gestionnaire technique"),
    ("Julie Renard", "j.renard@elron-gestion.fr", "Comptable"),
    ("Alexandre Morel", "a.morel@elron-gestion.fr", "Gestionnaire locatif"),
    ("Nadia Hamdi", "n.hamdi@elron-gestion.fr", "Assistante de gestion"),
]

FR_OWNERS = [
    ("Philippe de Villiers", "p.devilliers@orange.fr", "Rés. Les Tilleuls"),
    ("Marie-Claire Fontaine", "mc.fontaine@sfr.fr", "8 avenue Foch"),
    ("SCI Les Platanes", "sci.platanes@gmail.com", "23 rue Voltaire"),
    ("Jean-Marc Delacroix", "jm.delacroix@free.fr", "15 rue des Lilas"),
    ("SCI Garonne Patrimoine", "contact@garonne-patrimoine.fr", "42 bd Gambetta + 5 impasse des Acacias"),
    ("André Blanchard", "a.blanchard.immo@gmail.com", "17 rue du Marché"),
    ("SCI Clos Fleuri Invest", "gestion@closfleuri-invest.fr", "Rés. Le Clos Fleuri"),
]

# ---------------------------------------------------------------------------
# STORYLINES — conversations threadées
# ---------------------------------------------------------------------------
FR_STORYLINES = []

# === 1. FUITE CUISINE — 15 rue des Lilas, Apt 3B (Mme Petit) ===
FR_STORYLINES.append({
    "id": "fuite_cuisine",
    "thread_subject": "Fuite robinet cuisine - 15 rue des Lilas Apt 3B",
    "emails": [
        {
            "archived": True,
            "from_name": "Marie Petit",
            "from_email": "m.petit.locataire@gmail.com",
            "subject": "Fuite robinet cuisine - 15 rue des Lilas Apt 3B",
            "body": "Bonjour,\n\nJe vous écris car j'ai une fuite au niveau du robinet de la cuisine. Ça goutte en permanence depuis hier soir, j'ai mis une bassine en dessous mais c'est pas une solution.\n\nPourriez-vous envoyer un plombier svp ?\n\nMerci,\nMarie Petit\nAppartement 3B",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Fuite robinet cuisine - 15 rue des Lilas Apt 3B",
            "body": "Bonjour Madame Petit,\n\nMerci pour votre signalement. J'ai contacté notre plombier (Duplex Plomberie) qui devrait pouvoir passer cette semaine.\n\nJe vous tiens au courant dès que j'ai un créneau.\n\nCordialement,\nAlexandre Morel\nGestionnaire locatif - Elron Gestion",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Duplex Plomberie",
            "from_email": "contact@duplex-plomberie.fr",
            "subject": "Re: Fuite robinet cuisine - 15 rue des Lilas Apt 3B",
            "body": "Bonjour M. Morel,\n\nSuite à votre appel, je vous confirme que nous pouvons intervenir jeudi entre 14h et 16h.\n\nAprès échange téléphonique avec la locataire, il s'agit probablement d'un joint de robinet mitigeur à remplacer.\n\nDevis estimatif :\n- Déplacement : 45,00 € HT\n- Main d'œuvre (1h) : 55,00 € HT\n- Fournitures (joint + cartouche si nécessaire) : 25,00 à 80,00 € HT\n\nTotal estimé : 125,00 à 180,00 € TTC\n\nMerci de confirmer.\n\nCordialement,\nMarc Duplex\nDuplex Plomberie\n\n---\n📎 Pièce jointe : devis_EST_2025-0847.pdf (132 Ko)",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Fwd: Fuite robinet cuisine - 15 rue des Lilas Apt 3B - Devis plombier",
            "body": "Bonjour M. Delacroix,\n\nVeuillez trouver ci-dessous le devis du plombier pour la fuite chez Mme Petit (Apt 3B, 15 rue des Lilas).\n\nMontant estimé entre 125 et 180€ TTC. C'est de l'entretien courant, ça reste à la charge du propriétaire.\n\nPouvez-vous valider pour que je confirme l'intervention ?\n\nCordialement,\nAlexandre Morel",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Jean-Marc Delacroix",
            "from_email": "jm.delacroix@free.fr",
            "subject": "Re: Fuite robinet cuisine - 15 rue des Lilas Apt 3B - Devis plombier",
            "body": "Ok validé.\n\nFaites intervenir.\n\nJM Delacroix",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Duplex Plomberie",
            "from_email": "contact@duplex-plomberie.fr",
            "subject": "Intervention effectuée - 15 rue des Lilas Apt 3B",
            "body": "Bonjour,\n\nIntervention réalisée ce jour au 15 rue des Lilas, Apt 3B.\n\nDiagnostic : cartouche céramique du mitigeur HS.\nRemplacement effectué + vérification étanchéité OK.\n\nFacture ci-jointe :\n- Déplacement : 45,00 € HT\n- Main d'œuvre (45 min) : 55,00 € HT\n- Cartouche céramique 35mm : 42,00 € HT\nTotal HT : 142,00 €\nTVA 10% : 14,20 €\nTotal TTC : 156,20 €\n\nRèglement sous 30 jours.\n\nCordialement,\nMarc Duplex\n\n---\n📎 Pièce jointe : facture_FAC-2025-0391.pdf (98 Ko)",
            "is_reply": False,
        },
    ],
})

# === 2. IMPAYÉS LOYER — M. Benamara, 23 rue Voltaire ===
FR_STORYLINES.append({
    "id": "impayes_benamara",
    "thread_subject": "Loyer impayé novembre - M. Benamara, 23 rue Voltaire Apt 4A",
    "emails": [
        {
            "archived": True,
            "from_name": "Julie Renard",
            "from_email": "j.renard@elron-gestion.fr",
            "subject": "Loyer impayé novembre - M. Benamara, 23 rue Voltaire Apt 4A",
            "body": "Bonjour Alexandre,\n\nJe n'ai pas reçu le loyer de M. Benamara (Apt 4A, 23 rue Voltaire) pour le mois de novembre. C'est le 2ème mois consécutif — octobre n'a été régularisé que le 22/10.\n\nMontant dû : 720,00 € (loyer 650€ + charges 70€)\n\nPeux-tu le relancer stp ? Si pas de régularisation rapide il faudra qu'on envisage une procédure.\n\nMerci,\nJulie",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Rappel loyer novembre",
            "body": "Bonjour Monsieur Benamara,\n\nSauf erreur de notre part, nous n'avons pas reçu votre règlement de loyer pour le mois de novembre 2025.\n\nMontant : 720,00 € (loyer + charges)\nÉchéance : 05/11/2025\n\nNous vous remercions de bien vouloir procéder au règlement dans les meilleurs délais. En cas de difficulté, n'hésitez pas à nous contacter pour trouver une solution.\n\nCordialement,\nAlexandre Morel\nElron Gestion Immobilière",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Karim Benamara",
            "from_email": "k.benamara.loc@gmail.com",
            "subject": "Re: Rappel loyer novembre",
            "body": "Bonjour M. Morel\n\nDésolé pour le retard je sais que c'est pas la première fois. J'ai eu des soucis au boulot, j'ai été en arrêt maladie 3 semaines et ça a décalé ma paie.\n\nJe peux pas tout payer d'un coup mais je peux faire un virement de 400€ cette semaine et le reste fin décembre. Est ce que c'est possible ?\n\nMerci de votre compréhension\nK. Benamara",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Rappel loyer novembre",
            "body": "Bonjour Monsieur Benamara,\n\nJe comprends votre situation. Voici ce que je vous propose :\n\n- 400€ avant le 6 décembre (novembre - 1er versement)\n- 320€ avant le 20 décembre (solde novembre)\n- Loyer de décembre (720€) à l'échéance normale du 5 janvier\n\nMerci de me confirmer par retour de mail que cet échéancier vous convient. Je vous enverrai un courrier de confirmation.\n\nAttention : tout nouveau retard nous obligerait à engager une procédure.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Karim Benamara",
            "from_email": "k.benamara.loc@gmail.com",
            "subject": "Re: Rappel loyer novembre",
            "body": "Oui c'est bon pour moi merci. Je fais le virement de 400 demain.\n\nBenamara",
            "is_reply": True,
        },
    ],
})

# === 3. ASCENSEUR EN PANNE — Rés. Les Tilleuls (2 threads séparés) ===
FR_STORYLINES.append({
    "id": "ascenseur_leroy",
    "thread_subject": "Ascenseur en panne - Résidence Les Tilleuls",
    "emails": [
        {
            "archived": True,
            "from_name": "Patrick Leroy",
            "from_email": "p.leroy.locataire@gmail.com",
            "subject": "Ascenseur en panne - Résidence Les Tilleuls",
            "body": "Bonjour,\n\nL'ascenseur de la résidence Les Tilleuls est en panne depuis ce matin. Les portes s'ouvrent mais la cabine ne bouge plus.\n\nJe suis au 6ème étage et j'ai 73 ans, c'est vraiment compliqué pour moi de monter à pied. Merci de faire le nécessaire en urgence.\n\nP. Leroy - Apt 6C",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Ascenseur en panne - Résidence Les Tilleuls",
            "body": "Bonjour M. Leroy,\n\nJ'ai bien noté votre signalement. Azur Ascenseurs a été contacté, un technicien passera cet après-midi.\n\nJe vous tiens informé.\n\nCordialement,\nThomas Lefèvre\nGestionnaire technique",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Azur Ascenseurs",
            "from_email": "service@azur-ascenseurs.fr",
            "subject": "Re: Ascenseur en panne - Résidence Les Tilleuls",
            "body": "Bonjour M. Lefèvre,\n\nNotre technicien est intervenu ce jour. Diagnostic : carte électronique de commande défaillante.\n\nLa pièce doit être commandée (délai 3-5 jours ouvrés). L'ascenseur restera immobilisé pendant ce temps.\n\nDevis réparation :\n- Carte électronique Otis MCS220 : 1 250,00 € HT\n- Main d'œuvre pose et programmation (2h) : 180,00 € HT\n- Déplacement diagnostic : offert (contrat de maintenance)\nTotal HT : 1 430,00 €\nTVA 20% : 286,00 €\nTotal TTC : 1 716,00 €\n\nMerci de valider pour commande de la pièce.\n\nCordialement,\nSébastien Mercier\nAzur Ascenseurs\n\n---\n📎 Pièce jointe : devis_AZR-2025-1203.pdf (156 Ko)\n📎 Pièce jointe : rapport_intervention_20251218.pdf (89 Ko)",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Ascenseur en panne - Résidence Les Tilleuls",
            "body": "Thomas,\n\nOK pour le devis Azur, valide la commande de la pièce.\n\nPeux-tu afficher une note dans le hall pour prévenir tous les locataires du délai de réparation ?\n\nAlexandre",
            "is_reply": True,
        },
    ],
})

FR_STORYLINES.append({
    "id": "ascenseur_diallo",
    "thread_subject": "Problème ascenseur résidence les tilleuls",
    "emails": [
        {
            "archived": True,
            "from_name": "Amina Diallo",
            "from_email": "a.diallo.loc@gmail.com",
            "subject": "Problème ascenseur résidence les tilleuls",
            "body": "bonjour\n\nlascenseur marche plus depuis ce matin. je suis au 3eme avec un bébé et une poussette cest galère. est ce que vous savez quand ça va etre réparé ?\n\nmerci\namina diallo apt 3A",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Problème ascenseur résidence les tilleuls",
            "body": "Bonjour Madame Diallo,\n\nL'ascenseur est effectivement en panne. Un technicien est passé aujourd'hui et a identifié le problème (une pièce électronique à remplacer).\n\nLa réparation est prévue dans un délai de 3 à 5 jours. Nous nous excusons pour la gêne occasionnée.\n\nCordialement,\nThomas Lefèvre",
            "is_reply": True,
        },
    ],
})

# === 4. RAVALEMENT FAÇADE — Rés. Le Clos Fleuri ===
FR_STORYLINES.append({
    "id": "ravalement_clos_fleuri",
    "thread_subject": "Ravalement façade - Résidence Le Clos Fleuri - Devis et planning",
    "emails": [
        {
            "archived": True,
            "from_name": "Peinture & Ravalement Girard",
            "from_email": "devis@girard-ravalement.fr",
            "subject": "Ravalement façade - Résidence Le Clos Fleuri - Devis et planning",
            "body": "Bonjour Madame Marchand,\n\nSuite à notre visite du site le 15/10, veuillez trouver ci-joint notre devis pour le ravalement de la façade de la Résidence Le Clos Fleuri.\n\nPrestations :\n- Montage/démontage échafaudage : 4 200 € HT\n- Nettoyage haute pression : 2 800 € HT\n- Rebouchage fissures et reprise d'enduit : 3 500 € HT\n- Application peinture minérale (2 couches) : 8 600 € HT\n- Traitement hydrofuge : 1 900 € HT\n\nTotal HT : 21 000,00 €\nTVA 10% : 2 100,00 €\nTotal TTC : 23 100,00 €\n\nDurée estimée des travaux : 4 à 5 semaines\nDémarrage possible : mars 2026\n\nCe devis est valable 3 mois.\n\nCordialement,\nPatrick Girard\nPeinture & Ravalement Girard\n\n---\n📎 Pièce jointe : devis_RAV-2025-0156.pdf (2.1 Mo)\n📎 Pièce jointe : references_chantiers.pdf (4.3 Mo)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Sophie Marchand",
            "from_email": "s.marchand@elron-gestion.fr",
            "subject": "Re: Ravalement façade - Résidence Le Clos Fleuri - Devis et planning",
            "body": "Thomas,\n\nTu as vu le devis Girard pour le ravalement du Clos Fleuri ? 23K€ TTC.\n\nC'est dans la fourchette de ce qu'on avait estimé. On a reçu les 2 autres devis (Durand à 26K et BTP Sud à 28K) donc Girard est le moins cher.\n\nJe propose qu'on présente les 3 devis à la SCI lors de la réunion de décembre. Tu peux préparer un comparatif ?\n\nSophie",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Ravalement façade - Résidence Le Clos Fleuri - Devis et planning",
            "body": "Oui je prépare ça.\n\nPar contre Girard n'a pas inclus la reprise des balcons, je leur demande un avenant ?\n\nThomas",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Sophie Marchand",
            "from_email": "s.marchand@elron-gestion.fr",
            "subject": "Re: Ravalement façade - Résidence Le Clos Fleuri - Devis et planning",
            "body": "Oui bonne idée, demande-leur un chiffrage séparé pour les balcons. Comme ça la SCI pourra décider si elle fait tout d'un coup ou en deux phases.\n\nMerci",
            "is_reply": True,
        },
    ],
})

# === 5. ÉTAT DES LIEUX SORTANT — Rodriguez ===
FR_STORYLINES.append({
    "id": "edl_rodriguez",
    "thread_subject": "Préavis de départ - A. Rodriguez - 5 impasse des Acacias Apt 1C",
    "emails": [
        {
            "archived": True,
            "from_name": "Antonio Rodriguez",
            "from_email": "a.rodriguez.tenant@gmail.com",
            "subject": "Préavis de départ - A. Rodriguez - 5 impasse des Acacias Apt 1C",
            "body": "Bonjour,\n\nPar la présente, je vous informe de mon intention de quitter le logement situé au 5 impasse des Acacias, appartement 1C, à Toulouse.\n\nConformément à mon bail, je respecte un préavis d'un mois. Ma date de sortie souhaitée est le 31 décembre 2025.\n\nJe reste disponible pour convenir d'un rendez-vous pour l'état des lieux de sortie.\n\nCordialement,\nAntonio Rodriguez\n\n---\n📎 Pièce jointe : courrier_preavis_rodriguez.pdf (45 Ko)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Préavis de départ - A. Rodriguez - 5 impasse des Acacias Apt 1C",
            "body": "Bonjour Monsieur Rodriguez,\n\nJ'accuse réception de votre préavis de départ. Votre préavis d'un mois courra à compter de la réception de ce mail, soit une fin de bail au 31 décembre 2025.\n\nJe vous propose les créneaux suivants pour l'état des lieux de sortie :\n- Lundi 29 décembre à 10h00\n- Mardi 30 décembre à 14h00\n- Mercredi 31 décembre à 9h00\n\nMerci de me confirmer votre préférence.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Antonio Rodriguez",
            "from_email": "a.rodriguez.tenant@gmail.com",
            "subject": "Re: Préavis de départ - A. Rodriguez - 5 impasse des Acacias Apt 1C",
            "body": "Le 30 à 14h c'est parfait pour moi.\n\nJe voudrais savoir aussi quand est-ce que je récupère mon dépôt de garantie ?\n\nMerci\nA. Rodriguez",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Préavis de départ - A. Rodriguez - 5 impasse des Acacias Apt 1C",
            "body": "Bonjour,\n\nC'est noté pour le 30/12 à 14h.\n\nConcernant le dépôt de garantie (650€), il vous sera restitué dans un délai maximum d'un mois après l'état des lieux de sortie si celui-ci est conforme. En cas de dégradations constatées, des retenues pourront être appliquées conformément à la loi.\n\nN'hésitez pas à nettoyer l'appartement et à reboucher les trous de fixation avant l'état des lieux.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
    ],
})

# === 6. NUISANCES SONORES — Mme Lambert ===
FR_STORYLINES.append({
    "id": "nuisances_lambert",
    "thread_subject": "Nuisances sonores insupportables - 15 rue des Lilas",
    "emails": [
        {
            "archived": True,
            "from_name": "Christine Lambert",
            "from_email": "c.lambert.appt@gmail.com",
            "subject": "Nuisances sonores insupportables - 15 rue des Lilas",
            "body": "Monsieur Morel,\n\nJe vous écris ENCORE une fois pour me plaindre du bruit venant de l'appartement du dessous (3B, Mme Petit). Musique à fond tous les week-ends jusqu'à 1h du matin, ça fait 3 semaines que ça dure.\n\nJ'ai frappé chez elle, elle m'a envoyée balader. Je n'en peux plus, je ne dors plus le samedi soir. Si rien n'est fait je vais devoir contacter un avocat.\n\nC. Lambert - Apt 4A",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Nuisances sonores insupportables - 15 rue des Lilas",
            "body": "Bonjour Madame Lambert,\n\nJe comprends votre frustration et je prends ce sujet au sérieux.\n\nJ'ai envoyé un courrier recommandé à Mme Petit lui rappelant les clauses du règlement intérieur concernant les nuisances sonores (respect du voisinage, interdiction de bruit excessif après 22h).\n\nJe vous recommande également, si les nuisances persistent, de contacter la police municipale lors des faits pour constituer un dossier.\n\nJe vous tiens informée des suites.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Christine Lambert",
            "from_email": "c.lambert.appt@gmail.com",
            "subject": "Re: Nuisances sonores insupportables - 15 rue des Lilas",
            "body": "Merci pour le courrier.\n\nJe voulais vous informer que le bruit a diminué cette semaine. Le samedi elle a quand même mis de la musique mais c'était supportable et ça s'est arrêté vers 23h. Je vais voir si ça dure.\n\nCordialement,\nC. Lambert",
            "is_reply": True,
        },
    ],
})

# === 7. RENOUVELLEMENT BAIL — Famille Dupont ===
FR_STORYLINES.append({
    "id": "bail_dupont",
    "thread_subject": "Renouvellement bail - Dupont - 8 avenue Foch Apt 2B",
    "emails": [
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Renouvellement bail - Dupont - 8 avenue Foch Apt 2B",
            "body": "Bonjour Monsieur et Madame Dupont,\n\nVotre bail arrive à échéance le 28 février 2026. Conformément à la loi, je vous informe que la propriétaire, Mme Fontaine, souhaite renouveler votre bail.\n\nLe loyer actuel de 1 150,00 € sera révisé selon l'IRL du 3ème trimestre 2025, soit une augmentation de 2,47%.\n\nNouveau loyer proposé : 1 178,41 € / mois (charges comprises : 1 328,41 €)\n\nMerci de me faire part de votre réponse avant le 15 janvier 2026.\n\nCordialement,\nAlexandre Morel\nElron Gestion\n\n---\n📎 Pièce jointe : proposition_renouvellement_bail_dupont.pdf (78 Ko)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Marc Dupont",
            "from_email": "m.dupont.locataire@gmail.com",
            "subject": "Re: Renouvellement bail - Dupont - 8 avenue Foch Apt 2B",
            "body": "Bonjour M. Morel,\n\nMerci pour cette information. Nous souhaitons effectivement rester dans l'appartement.\n\nCependant, nous avions signalé à plusieurs reprises le problème d'humidité dans la chambre (mur nord) qui n'a toujours pas été traité. Nous avons dû acheter un déshumidificateur à nos frais.\n\nSerait-il possible de conditionner le renouvellement à la réalisation de ces travaux ? Et dans ce cas, de maintenir le loyer actuel le temps que ce soit réglé ?\n\nCordialement,\nMarc & Sophie Dupont",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Renouvellement bail - Dupont - 8 avenue Foch Apt 2B",
            "body": "Bonjour,\n\nJ'ai transmis votre demande à Mme Fontaine. Elle accepte de faire réaliser un diagnostic humidité et les travaux nécessaires au printemps 2026.\n\nEn revanche, la révision de loyer selon l'IRL est légale et sera appliquée. Nous pouvons toutefois reporter la date d'effet de la révision au 1er avril 2026 (après les travaux).\n\nEst-ce que cela vous convient ?\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Marc Dupont",
            "from_email": "m.dupont.locataire@gmail.com",
            "subject": "Re: Renouvellement bail - Dupont - 8 avenue Foch Apt 2B",
            "body": "D'accord, c'est un compromis acceptable. On signe le renouvellement.\n\nMerci d'avoir fait le relais avec la propriétaire.\n\nCordialement,\nM. Dupont",
            "is_reply": True,
        },
    ],
})

# === 8. CHAUFFAGE COLLECTIF — Rés. Les Tilleuls ===
FR_STORYLINES.append({
    "id": "chauffage_tilleuls",
    "thread_subject": "Chauffage collectif en panne - Résidence Les Tilleuls",
    "emails": [
        {
            "archived": True,
            "from_name": "Olivier Mercier",
            "from_email": "o.mercier.loc@gmail.com",
            "subject": "Chauffage collectif en panne - Résidence Les Tilleuls",
            "body": "Bonjour,\n\nPlus de chauffage dans la résidence depuis hier soir. Il fait 14 degrés chez moi ce matin. On est en plein hiver, c'est pas normal.\n\nPlusieurs voisins m'ont dit qu'ils avaient le même problème, donc c'est bien la chaudière collective.\n\nMerci de faire venir quelqu'un en urgence.\n\nOlivier Mercier - Apt 5B",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Patrick Leroy",
            "from_email": "p.leroy.locataire@gmail.com",
            "subject": "Chauffage collectif en panne - Résidence Les Tilleuls",
            "body": "Re bonjour,\n\nJe me joins au signalement. Plus de chauffage depuis hier. À mon âge je ne peux pas rester dans le froid. Merci d'intervenir en urgence.\n\nP. Leroy Apt 6C",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Chauffage collectif en panne - Résidence Les Tilleuls",
            "body": "Bonjour à tous,\n\nLe chauffagiste ThermoConfort est prévenu et sera sur place dans les 2 heures.\n\nJe vous tiens informés.\n\nThomas Lefèvre\nGestionnaire technique",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "ThermoConfort SARL",
            "from_email": "devis@thermoconfort.fr",
            "subject": "Re: Chauffage collectif en panne - Résidence Les Tilleuls",
            "body": "M. Lefèvre,\n\nIntervention d'urgence effectuée ce matin.\n\nPanne identifiée : défaut sur le brûleur (électrode d'allumage + câble haute tension à remplacer). Réparation provisoire effectuée, le chauffage est remis en route.\n\nLes pièces définitives seront posées en début de semaine prochaine.\n\nFacture intervention urgence : 320,00 € TTC\nDevis remplacement pièces : 485,00 € TTC\n\nCordialement,\nJérôme Tissier\nThermoConfort\n\n---\n📎 Pièce jointe : rapport_intervention_TC-2025-12-19.pdf (145 Ko)",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Chauffage collectif en panne - Résidence Les Tilleuls",
            "body": "Merci Thomas. OK pour le remplacement des pièces, valide avec ThermoConfort.\n\nM. Leroy, M. Mercier : le chauffage est remis en route. N'hésitez pas à me signaler si le problème persiste.\n\nAlexandre Morel",
            "is_reply": True,
        },
    ],
})

# === 9. DÉGÂT DES EAUX — 8 av Foch, Apt 2A ===
FR_STORYLINES.append({
    "id": "degat_eaux_martin",
    "thread_subject": "Dégât des eaux - 8 avenue Foch Apt 2A",
    "emails": [
        {
            "archived": True,
            "from_name": "Isabelle Martin",
            "from_email": "i.martin.locataire@gmail.com",
            "subject": "Dégât des eaux - 8 avenue Foch Apt 2A",
            "body": "Bonjour,\n\nJ'ai un gros problème d'infiltration d'eau dans ma salle de bain. Le plafond est gonflé et de l'eau coule le long du mur. Je pense que ça vient de l'appartement du dessus.\n\nJ'ai pris des photos. C'est urgent, le plafond menace de tomber.\n\nMerci d'intervenir rapidement.\n\nIsabelle Martin\nApt 2A, 8 avenue Foch\n\n---\n📎 Pièce jointe : photos_degat_eaux_1.jpg (1.2 Mo)\n📎 Pièce jointe : photos_degat_eaux_2.jpg (980 Ko)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Dégât des eaux - 8 avenue Foch Apt 2A",
            "body": "Bonjour Madame Martin,\n\nMerci pour les photos. J'ai immédiatement :\n1. Contacté le plombier pour une recherche de fuite en urgence\n2. Prévenu l'occupant de l'appartement 3A (au-dessus)\n3. Ouvert un dossier sinistre auprès de l'assurance de l'immeuble\n\nVous devez de votre côté déclarer le sinistre à votre propre assurance habitation dans les 5 jours.\n\nVoici le numéro de déclaration côté propriétaire : SIN-2025-1207-003\n\nJe reviens vers vous très vite.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Dégât des eaux 8 av Foch - Constat amiable et expertise",
            "body": "Bonjour Madame Fontaine,\n\nJe vous informe d'un dégât des eaux survenu dans l'appartement 2A (Mme Martin). L'infiltration provient vraisemblablement de l'appartement 3A au-dessus.\n\nLa déclaration de sinistre a été faite (réf. SIN-2025-1207-003). L'assureur envoie un expert le 15/12.\n\nLe plombier a identifié une fuite sur un raccord de la douche du 3A. La réparation a été faite (210€ TTC).\n\nReste à chiffrer : reprise du plafond et peinture dans le 2A. Je vous ferai suivre le devis.\n\nCordialement,\nAlexandre Morel\n\n---\n📎 Pièce jointe : declaration_sinistre_SIN-2025-1207-003.pdf (67 Ko)\n📎 Pièce jointe : constat_amiable_degat_eaux.pdf (234 Ko)",
            "is_reply": False,
        },
    ],
})

# === 10. RÉUNION D'ÉQUIPE ===
FR_STORYLINES.append({
    "id": "reunion_equipe_jan",
    "thread_subject": "Réunion d'équipe - Point hebdo du 13/01",
    "emails": [
        {
            "archived": True,
            "from_name": "Sophie Marchand",
            "from_email": "s.marchand@elron-gestion.fr",
            "subject": "Réunion d'équipe - Point hebdo du 13/01",
            "body": "Bonjour à tous,\n\nRappel : réunion d'équipe lundi 13 janvier à 9h30 en salle de réunion.\n\nOrdre du jour :\n1. Point sur les impayés du trimestre (Julie)\n2. Planning travaux janvier-mars (Thomas)\n3. Nouveaux mandats (Alexandre)\n4. Questions diverses\n\nMerci de préparer vos points.\n\nSophie",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Sophie Marchand",
            "from_email": "s.marchand@elron-gestion.fr",
            "subject": "CR Réunion d'équipe - 13/01",
            "body": "Bonjour,\n\nVoici le CR de notre réunion du 13/01 :\n\n1. IMPAYÉS : 3 dossiers en cours (Benamara en plan d'apurement OK, Garnier relancé par LRAR, Fournier RDV pris). Total impayés : 2 890€.\n\n2. TRAVAUX :\n- Ravalement Clos Fleuri : vote AG prévu en février\n- Ascenseur Tilleuls : pièce commandée, réparation semaine prochaine\n- Chauffage Tilleuls : réparation définitive OK\n\n3. NOUVEAUX MANDATS : 2 prospects en cours (appart T3 rue de la Paix + local commercial bd Haussmann)\n\n4. DIVERS :\n- Nadia : nouveau logiciel de gestion → formation prévue le 20/01\n- Thomas : stock de clés à refaire pour les parties communes\n\nActions :\n→ Julie : relancer assurance dégât eaux 8 av Foch\n→ Alexandre : réponse candidatures 17 rue du Marché\n→ Thomas : planifier diagnostic humidité 8 av Foch (Dupont)\n\nBonne semaine,\nSophie",
            "is_reply": False,
        },
    ],
})

# === 11. PARKING — M. Bernard ===
FR_STORYLINES.append({
    "id": "parking_bernard",
    "thread_subject": "Place de parking occupée - Rés. Le Clos Fleuri",
    "emails": [
        {
            "archived": True,
            "from_name": "François Bernard",
            "from_email": "f.bernard.loc@gmail.com",
            "subject": "Place de parking occupée - Rés. Le Clos Fleuri",
            "body": "Bonjour,\n\nÇa fait la 3ème fois ce mois-ci que je retrouve une voiture garée sur MA place de parking (place n°12). C'est toujours la même voiture, une Peugeot 308 grise.\n\nJ'ai mis un mot sur le pare-brise mais rien ne change. C'est inadmissible, je paye 80€/mois pour cette place.\n\nMerci de régler ce problème rapidement.\n\nF. Bernard - Apt 3A",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Nadia Hamdi",
            "from_email": "n.hamdi@elron-gestion.fr",
            "subject": "Re: Place de parking occupée - Rés. Le Clos Fleuri",
            "body": "Bonjour Monsieur Bernard,\n\nJ'ai vérifié l'attribution des places. La Peugeot 308 grise semble appartenir à un visiteur régulier de Mme Garnier (Apt 2C).\n\nJ'ai affiché une note dans le hall et envoyé un mail à Mme Garnier pour lui rappeler que les places sont nominatives. Si le problème persiste, nous mettrons en place un plot amovible sur votre place.\n\nCordialement,\nNadia Hamdi\nAssistante de gestion",
            "is_reply": True,
        },
    ],
})

# === 12. SERRURE — M. Nguyen ===
FR_STORYLINES.append({
    "id": "serrure_nguyen",
    "thread_subject": "Changement serrure porte entrée - 23 rue Voltaire Apt 2C",
    "emails": [
        {
            "archived": True,
            "from_name": "Tran Nguyen",
            "from_email": "t.nguyen.loc@gmail.com",
            "subject": "Changement serrure porte entrée - 23 rue Voltaire Apt 2C",
            "body": "Bonjour,\n\nJe me suis fait cambrioler ce week-end. La police est venue et a fait un constat. La serrure de la porte d'entrée est cassée (forcée).\n\nJ'ai besoin qu'un serrurier change la serrure en urgence. J'ai posé une planche en attendant mais c'est pas sécurisé.\n\nMerci\nT. Nguyen\n\n---\n📎 Pièce jointe : depot_plainte_20251205.pdf (156 Ko)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Changement serrure porte entrée - 23 rue Voltaire Apt 2C",
            "body": "Bonjour M. Nguyen,\n\nDésolé pour ce qui vous est arrivé. J'ai contacté Serrures Express qui passera demain matin entre 8h et 10h.\n\nAttention : la serrure de la porte d'entrée est à la charge du locataire (sauf si c'est un défaut de sécurité de l'immeuble). Mais vu les circonstances, voyez avec votre assurance habitation qui peut prendre en charge.\n\nBon courage,\nThomas Lefèvre",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Serrures Express",
            "from_email": "contact@serrures-express.fr",
            "subject": "Intervention serrurerie - 23 rue Voltaire Apt 2C - Facture",
            "body": "Bonjour,\n\nIntervention effectuée ce jour.\n\nTravaux réalisés :\n- Dépose ancienne serrure (cylindre européen forcé)\n- Pose nouveau cylindre haute sécurité Vachette\n- Remise de 3 clés + carte de propriété\n- Test fonctionnement OK\n\nFacture n° SE-2025-0934 :\n- Déplacement urgence : 60,00 € HT\n- Main d'œuvre : 85,00 € HT\n- Cylindre Vachette haute sécurité : 120,00 € HT\nTotal HT : 265,00 €\nTVA 20% : 53,00 €\nTotal TTC : 318,00 €\n\nCordialement,\nSerrures Express\n\n---\n📎 Pièce jointe : facture_SE-2025-0934.pdf (87 Ko)",
            "is_reply": False,
        },
    ],
})

# === 13. CAFARDS — Mme Moreau ===
FR_STORYLINES.append({
    "id": "cafards_moreau",
    "thread_subject": "Invasion cafards - 17 rue du Marché Apt 1A",
    "emails": [
        {
            "archived": True,
            "from_name": "Catherine Moreau",
            "from_email": "c.moreau.loc@gmail.com",
            "subject": "Invasion cafards - 17 rue du Marché Apt 1A",
            "body": "Bonjour\n\nJ'ai des cafards dans ma cuisine c'est DÉGOUTANT. J'en trouve tous les soirs quand j'allume la lumière, ils sont partout derrière le frigo et sous l'évier.\n\nJai acheté des pièges mais ça marche pas, y'en a de plus en plus. Je crois que ça vient des parties communes ou du local poubelles.\n\nFaut faire une désinsectisation de tout l'immeuble sinon ça sert à rien de traiter juste chez moi.\n\nC. Moreau",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Invasion cafards - 17 rue du Marché Apt 1A",
            "body": "Bonjour Madame Moreau,\n\nJ'ai contacté SOS Nuisibles pour une intervention. Ils préconisent effectivement un traitement de l'ensemble de l'immeuble pour être efficace.\n\nL'intervention est prévue le 18 décembre :\n- 9h-12h : parties communes (local poubelles, caves, couloirs)\n- 14h-17h : appartements (sur accord des occupants)\n\nUn courrier sera distribué à tous les résidents. Merci de vous assurer que la cuisine et la salle de bain sont accessibles.\n\nCordialement,\nThomas Lefèvre",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Invasion cafards - 17 rue du Marché Apt 1A",
            "body": "Mme Moreau,\n\nPour info, l'intervention est confirmée pour le 18/12. Nadia va distribuer un courrier à tous les résidents.\n\nN'hésitez pas à me contacter si vous avez des questions.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "SOS Nuisibles",
            "from_email": "intervention@sos-nuisibles.fr",
            "subject": "Compte-rendu intervention - 17 rue du Marché",
            "body": "Bonjour M. Lefèvre,\n\nCompte-rendu de l'intervention du 18/12/2025 au 17 rue du Marché, Nantes.\n\nTraitement réalisé :\n- Application gel anti-blattes dans parties communes\n- Traitement 4 appartements sur 6 (2 absents malgré notification)\n- Pose de pièges monitoring dans local poubelles\n\nConstats :\n- Infestation modérée, foyer principal identifié dans le local poubelles (défaut d'étanchéité du bac)\n- Recommandation : reboucher les passages de gaines dans les parties communes\n\nUne visite de contrôle est prévue dans 3 semaines.\n\nFacture : 680,00 € TTC\n\nCordialement,\nSOS Nuisibles\n\n---\n📎 Pièce jointe : CR_intervention_17ruedumarche.pdf (312 Ko)\n📎 Pièce jointe : facture_SOSN-2025-0287.pdf (56 Ko)",
            "is_reply": False,
        },
    ],
})

# === 14. FISSURE MUR — M. Dubois ===
FR_STORYLINES.append({
    "id": "fissure_dubois",
    "thread_subject": "Fissure importante mur salon - 42 bd Gambetta Apt 5B",
    "emails": [
        {
            "archived": True,
            "from_name": "Jean-Pierre Dubois",
            "from_email": "jp.dubois.loc@gmail.com",
            "subject": "Fissure importante mur salon - 42 bd Gambetta Apt 5B",
            "body": "Bonjour,\n\nUne fissure est apparue sur le mur du salon de mon appartement. Elle fait environ 40cm de long et semble s'agrandir depuis quelques semaines. On voit une légère ouverture.\n\nJe ne sais pas si c'est structurel ou juste de la peinture. Pouvez-vous envoyer quelqu'un pour vérifier ?\n\nVoir photos en pièce jointe.\n\nCordialement,\nJP Dubois\n\n---\n📎 Pièce jointe : fissure_salon_1.jpg (1.4 Mo)\n📎 Pièce jointe : fissure_salon_2.jpg (1.1 Mo)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Fissure importante mur salon - 42 bd Gambetta Apt 5B",
            "body": "Bonjour M. Dubois,\n\nMerci pour les photos. Vu l'aspect de la fissure, je pense qu'il faudrait un diagnostic par un expert. J'ai demandé un devis à ABC Diagnostics.\n\nEn attendant, ce n'est probablement pas dangereux mais évitez de percer ou clouer dans cette zone.\n\nJe reviens vers vous.\n\nCordialement,\nThomas Lefèvre",
            "is_reply": True,
        },
    ],
})

# === 15. FIBRE OPTIQUE — Rés. Les Tilleuls ===
FR_STORYLINES.append({
    "id": "fibre_tilleuls",
    "thread_subject": "Installation fibre optique - Résidence Les Tilleuls",
    "emails": [
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Installation fibre optique - Résidence Les Tilleuls",
            "body": "Bonjour à tous,\n\nJe vous informe que l'opérateur Orange va procéder à l'installation de la fibre optique dans la résidence Les Tilleuls.\n\nLe passage des câbles dans les parties communes est prévu la semaine du 6 janvier 2026. Les travaux dans les logements seront à programmer individuellement avec l'opérateur de votre choix.\n\nMerci de ne pas toucher aux boîtiers installés dans les couloirs.\n\nCordialement,\nThomas Lefèvre\nGestionnaire technique",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Amina Diallo",
            "from_email": "a.diallo.loc@gmail.com",
            "subject": "Re: Installation fibre optique - Résidence Les Tilleuls",
            "body": "bonjour\n\nest ce que je peux choisir un autre opérateur que orange ? je suis chez free et je voudrais rester chez free.\n\nmerci\namina",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Installation fibre optique - Résidence Les Tilleuls",
            "body": "Bonjour Madame Diallo,\n\nOui tout à fait, Orange installe juste le réseau dans les parties communes mais vous êtes libre de choisir n'importe quel opérateur (Free, SFR, Bouygues...) pour votre raccordement individuel.\n\nCordialement,\nThomas Lefèvre",
            "is_reply": True,
        },
    ],
})

# === 16. COMPTEUR EAU — standalone referencing thread ===
FR_STORYLINES.append({
    "id": "compteur_eau_tilleuls",
    "thread_subject": "Relevé compteurs eau - Résidence Les Tilleuls",
    "emails": [
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Relevé compteurs eau - Résidence Les Tilleuls",
            "body": "Julie,\n\nJ'ai fait le relevé des compteurs d'eau individuels aux Tilleuls vendredi dernier. Le tableau est en pièce jointe.\n\nA noter : consommation anormalement élevée Apt 5B (Mercier). Possible fuite non détectée. Je vais le prévenir.\n\nThomas\n\n---\n📎 Pièce jointe : releve_compteurs_tilleuls_dec2025.xlsx (34 Ko)",
            "is_reply": False,
        },
    ],
})

# === INBOX THREADS (recent, in inbox — mix of short/long, with/without PJ) ===

# === 17. LONG THREAD — Fuite colonne montante 15 rue des Lilas (7 msgs, mixed archived/inbox) ===
FR_STORYLINES.append({
    "id": "fuite_colonne_lilas",
    "thread_subject": "Fuite colonne montante 15 rue des Lilas",
    "emails": [
        {
            "archived": True,
            "from_name": "Christine Lambert",
            "from_email": "c.lambert.appt@gmail.com",
            "subject": "Fuite colonne montante 15 rue des Lilas",
            "body": "Bonjour,\n\nIl y a une fuite d'eau dans le couloir du 3ème étage, entre l'appartement 3B et le 4A. L'eau coule le long du mur près de la colonne montante.\n\nC. Lambert Apt 4A",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Fuite colonne montante 15 rue des Lilas",
            "body": "Bonjour Mme Lambert,\n\nMerci pour le signalement. Je contacte le plombier immédiatement.\n\nThomas, tu peux passer sur place voir l'étendue des dégâts ?\n\nAlexandre",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Fuite colonne montante 15 rue des Lilas",
            "body": "J'y suis. C'est la colonne montante entre le 3ème et 4ème. Fuite sur un raccord cuivre. Duplex Plomberie peut venir demain matin.\n\nJ'ai coupé l'eau de la colonne en attendant.\n\nThomas",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Fuite colonne montante 15 rue des Lilas",
            "body": "OK merci. Préviens les locataires du 3ème et 4ème qu'il n'y aura pas d'eau ce soir sur cette colonne.\n\nJe préviens Delacroix (proprio).\n\nAlexandre",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Duplex Plomberie",
            "from_email": "contact@duplex-plomberie.fr",
            "subject": "Re: Fuite colonne montante 15 rue des Lilas",
            "body": "Bonjour,\n\nIntervention effectuée ce matin. Le raccord cuivre était corrodé, remplacement complet du tronçon (environ 60cm).\n\nL'eau est rétablie. RAS sur les autres raccords de la colonne.\n\nFacture ci-jointe.\n\nCordialement,\nDuplex Plomberie\n\n---\n📎 Pièce jointe : facture_FAC-2026-0042.pdf (87 Ko)\n📎 Pièce jointe : photos_intervention_colonne.pdf (1.4 Mo)",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Fuite colonne montante 15 rue des Lilas",
            "body": "Merci. Thomas, tu peux vérifier qu'il n'y a pas de dégâts dans les apparts ?\n\nMme Lambert, Mme Petit : est-ce que tout est OK chez vous après la réparation ? Pas de traces d'humidité ?\n\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Christine Lambert",
            "from_email": "c.lambert.appt@gmail.com",
            "subject": "Re: Fuite colonne montante 15 rue des Lilas",
            "body": "Bonjour M. Morel,\n\nChez moi c'est OK, pas de dégât. Par contre le mur du couloir est encore humide et la peinture commence à cloquer. Il faudra prévoir une reprise de peinture.\n\nCordialement,\nC. Lambert",
            "is_reply": True,
        },
    ],
})

# === 18. LONG THREAD — Chauffage Les Tilleuls v2 (6 msgs, multi-PJ, mixed) ===
FR_STORYLINES.append({
    "id": "chauffage_v2_mercier",
    "thread_subject": "Chauffage toujours pas réparé correctement - Les Tilleuls",
    "emails": [
        {
            "archived": True,
            "from_name": "Olivier Mercier",
            "from_email": "o.mercier.loc@gmail.com",
            "subject": "Chauffage toujours pas réparé correctement - Les Tilleuls",
            "body": "Bonjour,\n\nLe chauffage a été réparé en décembre mais depuis la semaine dernière ça recommence. Les radiateurs du salon et de la chambre sont tièdes au mieux. Il fait à peine 17 degrés chez moi.\n\nC'est quand même la 2ème fois cet hiver. Est-ce qu'il faudrait pas envisager de changer la chaudière ?\n\nO. Mercier",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Chauffage toujours pas réparé correctement - Les Tilleuls",
            "body": "Bonjour M. Mercier,\n\nDésolé pour ce désagrément. Je fais revenir ThermoConfort cette semaine.\n\nLa chaudière a 18 ans, on a effectivement commencé à demander des devis pour le remplacement. Je vous tiens au courant.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "ThermoConfort SARL",
            "from_email": "devis@thermoconfort.fr",
            "subject": "Re: Chauffage toujours pas réparé correctement - Les Tilleuls",
            "body": "Bonjour M. Morel,\n\nIntervention faite. Le circulateur est fatigué, il tourne mais ne pousse plus assez d'eau chaude. Remplacement nécessaire.\n\nDevis ci-joint pour le circulateur + purge complète du circuit.\n\nCordialement,\nThermoConfort\n\n---\n📎 Pièce jointe : devis_TC-2026-0089.pdf (67 Ko)\n📎 Pièce jointe : rapport_diagnostic_chauffage.pdf (234 Ko)",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Fwd: Chauffage toujours pas réparé correctement - Les Tilleuls",
            "body": "M. de Villiers,\n\nSuite à la nouvelle panne de chauffage, le chauffagiste propose le remplacement du circulateur (485€ TTC, devis en PJ).\n\nEn parallèle je vous ai envoyé les 3 devis pour le remplacement complet de la chaudière. Merci de me donner votre accord sur le circulateur en attendant votre décision sur la chaudière.\n\nCordialement,\nAlexandre Morel\n\n---\n📎 Pièce jointe : devis_TC-2026-0089.pdf (67 Ko)\n📎 Pièce jointe : comparatif_devis_chaudiere_tilleuls.pdf (234 Ko)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Philippe de Villiers",
            "from_email": "p.devilliers@orange.fr",
            "subject": "Re: Chauffage toujours pas réparé correctement - Les Tilleuls",
            "body": "OK pour le circulateur, faites le nécessaire.\n\nPour la chaudière, on prend le De Dietrich à 11 500€ comme convenu. Planifiez ça pour mars.\n\nCdt,\nPh. de Villiers",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Olivier Mercier",
            "from_email": "o.mercier.loc@gmail.com",
            "subject": "Re: Chauffage toujours pas réparé correctement - Les Tilleuls",
            "body": "Bonjour,\n\nDes nouvelles ? Le chauffage est toujours en panne chez moi. On est vendredi et personne n'est passé cette semaine.\n\nO. Mercier",
            "is_reply": True,
        },
    ],
})

# === 19. LONG THREAD — Dégât des eaux suivi assurance (6 msgs, multi-PJ) ===
FR_STORYLINES.append({
    "id": "degat_eaux_suivi",
    "thread_subject": "Suivi dégât des eaux 8 av Foch - Expertise et réparations",
    "emails": [
        {
            "archived": True,
            "from_name": "Groupama Assurances",
            "from_email": "mr.sinistres@groupama.fr",
            "subject": "Suivi dégât des eaux 8 av Foch - Expertise et réparations",
            "body": "Bonjour,\n\nSuite à l'expertise du 7 janvier, voici les conclusions de notre expert M. Leclercq :\n\n- Origine du sinistre : fuite raccord douche Apt 3A\n- Dommages Apt 2A : plafond SDB gonflé, peinture cloquée, traces humidité mur\n- Montant estimé des réparations : 2 340€ TTC\n\nRapport complet ci-joint. Merci de nous transmettre les devis de remise en état.\n\nCordialement,\nGroupama\n\n---\n📎 Pièce jointe : rapport_expertise_SIN-2025-1207-003.pdf (456 Ko)\n📎 Pièce jointe : photos_expertise.zip (3.2 Mo)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Suivi dégât des eaux 8 av Foch - Expertise et réparations",
            "body": "Bonjour,\n\nMerci pour le rapport. Je fais chiffrer les réparations par notre peintre et je vous transmets le devis.\n\nCordialement,\nAlexandre Morel\nElron Gestion",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Peinture & Ravalement Girard",
            "from_email": "devis@girard-ravalement.fr",
            "subject": "Devis reprise plafond et murs - 8 av Foch Apt 2A",
            "body": "Bonjour M. Morel,\n\nSuite à ma visite, voici le devis pour la reprise des dégâts :\n\n- Grattage et ponçage plafond SDB : 180€ HT\n- Application enduit de rebouchage : 120€ HT\n- Peinture plafond (2 couches) : 280€ HT\n- Reprise peinture mur (zone touchée) : 220€ HT\n- Traitement anti-humidité : 150€ HT\n\nTotal HT : 950€\nTVA 10% : 95€\nTotal TTC : 1 045€\n\nDisponibilité : semaine du 10 février.\n\nCordialement,\nP. Girard\n\n---\n📎 Pièce jointe : devis_GIR-2026-0023.pdf (78 Ko)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Fwd: Devis reprise plafond et murs - 8 av Foch Apt 2A",
            "body": "Mme Fontaine,\n\nVoici le devis du peintre pour la reprise des dégâts suite au dégât des eaux chez Mme Martin (Apt 2A). Montant : 1 045€ TTC.\n\nL'assurance devrait couvrir la majeure partie. Je transmets le devis à Groupama.\n\nCordialement,\nAlexandre Morel\n\n---\n📎 Pièce jointe : devis_GIR-2026-0023.pdf (78 Ko)\n📎 Pièce jointe : rapport_expertise_SIN-2025-1207-003.pdf (456 Ko)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Marie-Claire Fontaine",
            "from_email": "mc.fontaine@sfr.fr",
            "subject": "Re: Devis reprise plafond et murs - 8 av Foch Apt 2A",
            "body": "Bonjour M. Morel,\n\nD'accord pour le devis. Allez-y pour les travaux et transmettez à l'assurance.\n\nMerci pour le suivi.\n\nMC Fontaine",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Isabelle Martin",
            "from_email": "i.martin.locataire@gmail.com",
            "subject": "Re: Suivi dégât des eaux 8 av Foch - Expertise et réparations",
            "body": "Bonjour M. Morel,\n\nJ'ai vu qu'un peintre doit passer pour les réparations. Est-ce que vous avez une date ? Je dois poser un jour de congé pour être présente.\n\nAussi, le plafond de la SDB fait un drôle de bruit quand le voisin du dessus marche, c'est normal ?\n\nCordialement,\nI. Martin",
            "is_reply": True,
        },
    ],
})

# === 20. THREAD INBOX — Facture impayée prestataire (4 msgs) ===
FR_STORYLINES.append({
    "id": "facture_impayee_plombier",
    "thread_subject": "Relance facture FAC-2025-0391 - Duplex Plomberie",
    "emails": [
        {
            "archived": True,
            "from_name": "Duplex Plomberie",
            "from_email": "contact@duplex-plomberie.fr",
            "subject": "Relance facture FAC-2025-0391 - Duplex Plomberie",
            "body": "Bonjour,\n\n2ème relance pour la facture FAC-2025-0391 du 12/11/2025 (intervention 15 rue des Lilas, Apt 3B).\n\nMontant : 156,20 € TTC\nÉchéance dépassée de 45 jours.\n\nMerci de procéder au règlement dans les plus brefs délais.\n\nCordialement,\nService comptabilité\nDuplex Plomberie\n\n---\n📎 Pièce jointe : relance_FAC-2025-0391.pdf (43 Ko)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Relance facture FAC-2025-0391 - Duplex Plomberie",
            "body": "Bonjour,\n\nDésolé pour le retard. La facture est à la charge du propriétaire (M. Delacroix) et nous attendons sa provision. Je le relance aujourd'hui.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Julie Renard",
            "from_email": "j.renard@elron-gestion.fr",
            "subject": "Fwd: Relance facture FAC-2025-0391 - Duplex Plomberie",
            "body": "Alexandre,\n\nLe plombier nous relance encore. C'est la 3ème relance maintenant. Delacroix n'a toujours pas payé sa provision.\n\nOn fait quoi ? On avance le paiement et on se fait rembourser, ou on attend encore ?\n\nJulie",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Duplex Plomberie",
            "from_email": "contact@duplex-plomberie.fr",
            "subject": "Re: Relance facture FAC-2025-0391 - Duplex Plomberie",
            "body": "Bonjour,\n\n3ème et dernière relance. Sans règlement sous 15 jours, nous transmettrons le dossier à notre cabinet de recouvrement.\n\nCordialement,\nDuplex Plomberie\n\n---\n📎 Pièce jointe : mise_en_demeure_FAC-2025-0391.pdf (56 Ko)",
            "is_reply": True,
        },
    ],
})

# === 21. THREAD INBOX — Candidature locataire (5 msgs avec échanges) ===
FR_STORYLINES.append({
    "id": "candidature_nantes",
    "thread_subject": "Candidature location - T2 17 rue du Marché Apt 2B",
    "emails": [
        {
            "archived": True,
            "from_name": "Léa Bertrand",
            "from_email": "lea.bertrand.pro@gmail.com",
            "subject": "Candidature location - T2 17 rue du Marché Apt 2B",
            "body": "Bonjour,\n\nSuite à la visite du T2 au 17 rue du Marché (Apt 2B) samedi dernier, je souhaite déposer ma candidature.\n\nJe suis infirmière au CHU de Nantes, en CDI depuis 3 ans. Mon salaire net est de 2 200€/mois.\n\nVous trouverez ci-joint mon dossier complet.\n\nCordialement,\nLéa Bertrand\n\n---\n📎 Pièce jointe : dossier_candidature_bertrand.pdf (3.2 Mo)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Candidature location - T2 17 rue du Marché Apt 2B",
            "body": "Bonjour Mme Bertrand,\n\nMerci pour votre candidature, votre dossier est complet. Nous avons reçu plusieurs candidatures et nous reviendrons vers vous en début de semaine prochaine avec notre décision.\n\nCordialement,\nAlexandre Morel\nElron Gestion",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Fwd: Candidature location - T2 17 rue du Marché Apt 2B",
            "body": "Sophie,\n\nJ'ai reçu 3 dossiers pour le T2 du 17 rue du Marché :\n\n1. Léa Bertrand - infirmière CHU, CDI 3 ans, 2 200€ net → dossier solide\n2. M. et Mme Charpentier - enseignants, 2x CDI, 3 800€ net → très bon\n3. M. Koné - ingénieur, CDI récent (6 mois), 2 800€ net → garant nécessaire\n\nMon avis : les Charpentier sont le meilleur profil. Tu valides ?\n\nAlexandre",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Sophie Marchand",
            "from_email": "s.marchand@elron-gestion.fr",
            "subject": "Re: Candidature location - T2 17 rue du Marché Apt 2B",
            "body": "D'accord avec toi pour les Charpentier. Dossier solide, double CDI.\n\nPar contre vérifie les quittances de leur logement actuel et appelle leur propriétaire pour une référence. On fait ça proprement.\n\nSophie",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Léa Bertrand",
            "from_email": "lea.bertrand.pro@gmail.com",
            "subject": "Re: Candidature location - T2 17 rue du Marché Apt 2B",
            "body": "Bonjour M. Morel,\n\nJe me permets de vous relancer pour ma candidature au T2 du 17 rue du Marché. Avez-vous pris une décision ?\n\nJe suis toujours très intéressée par cet appartement.\n\nCordialement,\nLéa Bertrand",
            "is_reply": True,
        },
    ],
})

# === 22. THREAD INBOX — Régularisation charges (3 msgs) ===
FR_STORYLINES.append({
    "id": "regul_charges",
    "thread_subject": "Régularisation des charges 2025 - 8 avenue Foch",
    "emails": [
        {
            "archived": True,
            "from_name": "Julie Renard",
            "from_email": "j.renard@elron-gestion.fr",
            "subject": "Régularisation des charges 2025 - 8 avenue Foch",
            "body": "Bonjour Alexandre,\n\nJ'ai finalisé la régularisation des charges pour le 8 avenue Foch. Voici le récap :\n\n- Apt 2A (Martin) : trop-perçu de 89€, remboursement à faire\n- Apt 2B (Dupont) : complément de 156€ à appeler\n- Apt 3A (vacant) : RAS\n\nLes courriers sont prêts, tu veux les vérifier avant envoi ?\n\nJulie\n\n---\n📎 Pièce jointe : regul_charges_2025_8avFoch.xlsx (45 Ko)",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Régularisation des charges 2025 - 8 avenue Foch",
            "body": "Julie,\n\nC'est bon j'ai vérifié, tout est correct. Tu peux envoyer les courriers.\n\nPar contre préviens Mme Martin par mail pour le remboursement, elle me demandait justement des nouvelles.\n\nAlexandre",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Marc Dupont",
            "from_email": "m.dupont.locataire@gmail.com",
            "subject": "Re: Régularisation des charges 2025 - 8 avenue Foch",
            "body": "Bonjour,\n\nJ'ai reçu le courrier pour la régularisation de charges. 156€ de complément c'est quand même beaucoup. Est-ce que je pourrais avoir le détail des charges svp ? Surtout le poste chauffage, je trouve que l'immeuble est mal isolé et que ça revient cher.\n\nCordialement,\nM. Dupont",
            "is_reply": True,
        },
    ],
})

# === 23. LONG THREAD INBOX — Fuite d'eau 23 rue Voltaire (6 msgs) ===
FR_STORYLINES.append({
    "id": "fuite_voltaire_recent",
    "thread_subject": "Fuite d'eau importante - 23 rue Voltaire parties communes",
    "emails": [
        {
            "archived": True,
            "from_name": "Nathalie Simon",
            "from_email": "n.simon.loc@gmail.com",
            "subject": "Fuite d'eau importante - 23 rue Voltaire parties communes",
            "body": "BONJOUR\n\nIl y a une fuite d'eau dans le hall d'entrée du 23 rue voltaire !!! L'eau coule du plafond du hall, ça forme une flaque énorme devant les boites aux lettres.\n\nJ'ai mis des serpillières mais ça suffit pas. quelqu'un peut venir ???\n\nNathalie Simon Apt 1A",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Fuite d'eau importante - 23 rue Voltaire parties communes",
            "body": "Bonjour Mme Simon,\n\nMerci pour l'alerte. Thomas passe sur place dans l'heure et le plombier est prévenu.\n\nSi vous pouvez couper l'arrivée d'eau générale (vanne au sous-sol), ça limiterait les dégâts.\n\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Fuite d'eau importante - 23 rue Voltaire parties communes",
            "body": "Alexandre,\n\nJe suis sur place. La fuite vient du raccord de la vanne palière du 2ème étage. J'ai coupé l'eau. Duplex arrive dans 30 min.\n\nIl y a de l'eau dans le hall et un peu dans la cave. Photos en PJ.\n\nThomas\n\n---\n📎 Pièce jointe : photos_fuite_voltaire_1.jpg (1.8 Mo)\n📎 Pièce jointe : photos_fuite_voltaire_2.jpg (2.1 Mo)",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Fuite d'eau importante - 23 rue Voltaire parties communes",
            "body": "Reçu merci. Je préviens la SCI Les Platanes et j'ouvre un dossier assurance si nécessaire.",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Duplex Plomberie",
            "from_email": "contact@duplex-plomberie.fr",
            "subject": "Re: Fuite d'eau importante - 23 rue Voltaire parties communes",
            "body": "Bonjour,\n\nIntervention terminée. Remplacement de la vanne palière du 2ème étage et du raccord défectueux.\n\nL'eau est rétablie dans tout l'immeuble.\n\nFacture en PJ.\n\nCordialement,\nDuplex Plomberie\n\n---\n📎 Pièce jointe : facture_FAC-2026-0067.pdf (92 Ko)\n📎 Pièce jointe : rapport_intervention_voltaire.pdf (134 Ko)",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Nathalie Simon",
            "from_email": "n.simon.loc@gmail.com",
            "subject": "Re: Fuite d'eau importante - 23 rue Voltaire parties communes",
            "body": "merci pour la rapidité. par contre il y a encore des traces d'eau dans le hall et ça sent l'humidité. est ce que quelqu'un va nettoyer ?\n\nnathalie simon",
            "is_reply": True,
        },
    ],
})

# === 22. BOÎTE AUX LETTRES FORCÉE — Rés. Le Clos Fleuri ===
FR_STORYLINES.append({
    "id": "bal_forcee_clos_fleuri",
    "thread_subject": "Boîte aux lettres forcée - Rés. Le Clos Fleuri",
    "emails": [
        {
            "archived": True,
            "from_name": "Émilie Garnier",
            "from_email": "e.garnier.loc@gmail.com",
            "subject": "Boîte aux lettres forcée - Rés. Le Clos Fleuri",
            "body": "Bonjour,\n\nJe vous signale que ma boîte aux lettres a été forcée. La serrure est cassée et la porte ne ferme plus. J'ai retrouvé du courrier par terre dans le hall ce matin.\n\nC'est la deuxième fois en 6 mois, c'est vraiment pénible.\n\nMerci de faire intervenir un serrurier.\n\nE. Garnier\nApt 4D",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Nadia Hamdi",
            "from_email": "n.hamdi@elron-gestion.fr",
            "subject": "Re: Boîte aux lettres forcée - Rés. Le Clos Fleuri",
            "body": "Bonjour Mme Garnier,\n\nMerci pour le signalement. J'ai contacté Serrures Express, ils passeront demain entre 10h et 12h pour remplacer la serrure de votre boîte aux lettres.\n\nEn attendant, vous pouvez demander au gardien de récupérer votre courrier.\n\nCordialement,\nNadia Hamdi\nAssistante de gestion",
            "is_reply": True,
        },
    ],
})

# === 23. DEMANDE D'ANIMAUX DE COMPAGNIE — Mme Bouzid ===
FR_STORYLINES.append({
    "id": "animal_bouzid",
    "thread_subject": "Demande autorisation animal de compagnie - Apt 1B 15 rue des Lilas",
    "emails": [
        {
            "archived": True,
            "from_name": "Fatima Bouzid",
            "from_email": "f.bouzid.loc@gmail.com",
            "subject": "Demande autorisation animal de compagnie - Apt 1B 15 rue des Lilas",
            "body": "Bonjour\n\nje voudrais savoir si j'ai le droit d'avoir un chat dans l'appartement. Mes enfants en veulent un depuis longtemps. C'est un petit chat qui resterait en intérieur.\n\nmerci de me dire si c'est possible ou pas\n\nfatima bouzid\napt 1B 15 rue des lilas",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Demande autorisation animal de compagnie - Apt 1B 15 rue des Lilas",
            "body": "Bonjour Madame Bouzid,\n\nJ'ai vérifié votre bail. Il ne comporte pas de clause d'interdiction des animaux de compagnie (la loi du 9 juillet 1970 interdit d'ailleurs ce type de clause pour les animaux domestiques courants).\n\nVous pouvez donc adopter un chat sans problème, à condition qu'il ne cause pas de nuisances aux autres occupants.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Fatima Bouzid",
            "from_email": "f.bouzid.loc@gmail.com",
            "subject": "Re: Demande autorisation animal de compagnie - Apt 1B 15 rue des Lilas",
            "body": "super merci beaucoup !! les enfants vont etre contents 😊\n\nbonne journée\nfatima",
            "is_reply": True,
        },
    ],
})

# === 24. PROBLÈME VOISINAGE PARKING — 42 bd Gambetta ===
FR_STORYLINES.append({
    "id": "voisinage_parking_gambetta",
    "thread_subject": "Travaux bruyants voisin - 42 bd Gambetta Apt 3A",
    "emails": [
        {
            "archived": True,
            "from_name": "François Bernard",
            "from_email": "f.bernard.loc@gmail.com",
            "subject": "Travaux bruyants voisin - 42 bd Gambetta Apt 3A",
            "body": "Bonjour M. Morel,\n\nJe me permets de vous écrire car mon voisin du dessus (Apt 4A je pense) fait des travaux depuis 3 semaines. Perceuse, marteau, scie... du lundi au samedi, parfois jusqu'à 21h.\n\nJe travaille en télétravail et c'est devenu IMPOSSIBLE de travailler chez moi. Est-ce que ces travaux ont été déclarés ? Le règlement de copropriété prévoit des horaires non ?\n\nMerci d'intervenir.\n\nF. Bernard\nApt 3A",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Travaux bruyants voisin - 42 bd Gambetta Apt 3A",
            "body": "Bonjour M. Bernard,\n\nJ'ai bien pris note de votre plainte. L'appartement au-dessus du vôtre n'est pas géré par notre agence, mais j'ai contacté le syndic (Cabinet Gérard & Associés) pour signaler le problème.\n\nLe règlement de copropriété limite effectivement les travaux bruyants aux jours ouvrables de 8h à 19h et le samedi de 9h à 12h. Les travaux après 21h ne sont pas autorisés.\n\nLe syndic va envoyer un rappel au propriétaire concerné.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
    ],
})

# === 25. DÉPÔT DE GARANTIE RODRIGUEZ — RETOUR ===
FR_STORYLINES.append({
    "id": "depot_garantie_rodriguez",
    "thread_subject": "Remboursement dépôt de garantie - A. Rodriguez",
    "emails": [
        {
            "archived": True,
            "from_name": "Antonio Rodriguez",
            "from_email": "a.rodriguez.tenant@gmail.com",
            "subject": "Remboursement dépôt de garantie - A. Rodriguez",
            "body": "Bonjour M. Morel,\n\nJe reviens vers vous au sujet de mon dépôt de garantie (650€). J'ai quitté le logement le 31 décembre et l'état des lieux de sortie a été fait.\n\nVous m'aviez parlé de retenues éventuelles. Pourriez-vous me donner le détail et le montant du remboursement ?\n\nLe délai légal est d'un mois après la remise des clés il me semble.\n\nCordialement,\nA. Rodriguez",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Remboursement dépôt de garantie - A. Rodriguez",
            "body": "Bonjour M. Rodriguez,\n\nVoici le décompte de restitution de votre dépôt de garantie :\n\nDépôt versé : 650,00 €\n\nRetenues justifiées :\n- Rebouchage trous murs (x8) : 80,00 €\n- Remplacement plan de travail cuisine (brûlure) : 150,00 €\n- Nettoyage complet logement : 120,00 €\n\nTotal retenues : 350,00 €\nMontant à rembourser : 300,00 €\n\nLe virement sera effectué sous 10 jours ouvrés. Les justificatifs sont joints.\n\nCordialement,\nAlexandre Morel\n\n---\n📎 Pièce jointe : decompte_restitution_rodriguez.pdf (89 Ko)\n📎 Pièce jointe : factures_retenues_rodriguez.pdf (234 Ko)",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Antonio Rodriguez",
            "from_email": "a.rodriguez.tenant@gmail.com",
            "subject": "Re: Remboursement dépôt de garantie - A. Rodriguez",
            "body": "Bonjour,\n\nJe conteste la retenue de 150€ pour le plan de travail. La brûlure était là quand j'ai emménagé, ce n'est pas mentionné dans l'EDL d'entrée mais je m'en souviens très bien.\n\nPour les trous et le ménage, je ne discute pas.\n\nPouvez-vous revoir ce point ?\n\nCordialement,\nA. Rodriguez",
            "is_reply": True,
        },
    ],
})

# === 26. PROBLÈME DE CHAUFFE-EAU — Mme Simon ===
FR_STORYLINES.append({
    "id": "chauffe_eau_simon",
    "thread_subject": "Chauffe-eau qui fuit - 23 rue Voltaire Apt 1A",
    "emails": [
        {
            "archived": True,
            "from_name": "Nathalie Simon",
            "from_email": "n.simon.loc@gmail.com",
            "subject": "Chauffe-eau qui fuit - 23 rue Voltaire Apt 1A",
            "body": "Bonjour,\n\nMon ballon d'eau chaude fuit par le dessous. Il y a une flaque d'eau en permanence sous le cumulus et ça coule un peu le long du mur.\n\nJe mets des serpillères mais ça trempe le parquet. C'est assez urgent parce que l'eau est CHAUDE et j'ai peur que ça abîme le sol.\n\nMerci d'envoyer quelqu'un rapidement.\n\nNathalie Simon\nApt 1A, 23 rue Voltaire",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Chauffe-eau qui fuit - 23 rue Voltaire Apt 1A",
            "body": "Bonjour Mme Simon,\n\nMerci pour le signalement. En attendant l'intervention, pouvez-vous :\n1. Couper l'arrivée d'eau froide du ballon (vanne sous le cumulus)\n2. Couper l'alimentation électrique du cumulus au disjoncteur\n\nJ'ai contacté Duplex Plomberie, quelqu'un passera demain matin.\n\nCordialement,\nThomas Lefèvre",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Duplex Plomberie",
            "from_email": "contact@duplex-plomberie.fr",
            "subject": "Diagnostic chauffe-eau - 23 rue Voltaire Apt 1A",
            "body": "Bonjour M. Lefèvre,\n\nIntervention effectuée ce jour. Le ballon d'eau chaude (200L, marque Atlantic, installé en 2014) présente une fuite au niveau du groupe de sécurité ET une corrosion interne de la cuve.\n\nRéparation du groupe de sécurité possible (coût : ~120€ TTC) mais le ballon a 11 ans et la cuve est percée. Je recommande un remplacement complet.\n\nDevis remplacement :\n- Ballon Atlantic 200L Zénéo : 890€ HT\n- Dépose ancien + pose : 280€ HT\n- Raccordements + groupe sécurité neuf : 120€ HT\n- Mise en décharge ancien cumulus : 50€ HT\n\nTotal HT : 1 340,00 €\nTVA 10% : 134,00 €\nTotal TTC : 1 474,00 €\n\nDisponibilité : sous 3 jours après validation.\n\nCordialement,\nDuplex Plomberie\n\n---\n📎 Pièce jointe : devis_CE_2026-0021.pdf (145 Ko)\n📎 Pièce jointe : photos_cumulus_23voltaire.jpg (1.2 Mo)",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Nathalie Simon",
            "from_email": "n.simon.loc@gmail.com",
            "subject": "Re: Chauffe-eau qui fuit - 23 rue Voltaire Apt 1A",
            "body": "Bonjour\n\nMerci pour les consignes j'ai coupé l'eau et le disjoncteur. Par contre ça veut dire que j'ai plus d'eau chaude du tout. Le plombier est passé et il m'a dit que le ballon devait être remplacé.\n\nC'est prévu quand ? parce que se laver à l'eau froide en janvier c'est pas top...\n\nMerci\nN. Simon",
            "is_reply": True,
        },
    ],
})

# === 27. ASSURANCE HABITATION EXPIRÉE — Locataire Roux ===
FR_STORYLINES.append({
    "id": "assurance_expiree_roux",
    "thread_subject": "Relance assurance habitation - N. Roux, 17 rue du Marché",
    "emails": [
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Relance assurance habitation - N. Roux, 17 rue du Marché",
            "body": "Bonjour M. Roux,\n\nNous constatons que votre attestation d'assurance habitation a expiré le 30 novembre 2025. Or, en application de l'article 7g de la loi du 6 juillet 1989, tout locataire est tenu de justifier d'une assurance couvrant les risques locatifs.\n\nMerci de nous transmettre votre nouvelle attestation dans les meilleurs délais.\n\nÀ défaut de réponse sous 30 jours, nous serions contraints d'engager une procédure de résiliation de bail.\n\nCordialement,\nAlexandre Morel\nElron Gestion Immobilière",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Nicolas Roux",
            "from_email": "n.roux.tenant@gmail.com",
            "subject": "Re: Relance assurance habitation - N. Roux, 17 rue du Marché",
            "body": "Bonjour,\n\nDésolé pour le retard, j'ai changé d'assureur et ça a pris du temps. Je vous envoie la nouvelle attestation dès que je la reçois (normalement cette semaine).\n\nCordialement,\nN. Roux",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Nicolas Roux",
            "from_email": "n.roux.tenant@gmail.com",
            "subject": "Re: Relance assurance habitation - N. Roux, 17 rue du Marché",
            "body": "Re-bonjour,\n\nVoici l'attestation d'assurance habitation en pièce jointe. Contrat MATMUT n°AH-2026-04523, valable jusqu'au 31/12/2026.\n\nCordialement,\nN. Roux\n\n---\n📎 Pièce jointe : attestation_assurance_roux_2026.pdf (56 Ko)",
            "is_reply": True,
        },
    ],
})

# === 28. TRAVAUX PARTIES COMMUNES — Peinture cage d'escalier ===
FR_STORYLINES.append({
    "id": "peinture_cage_escalier",
    "thread_subject": "Devis peinture cage d'escalier - 15 rue des Lilas",
    "emails": [
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Devis peinture cage d'escalier - 15 rue des Lilas",
            "body": "Sophie,\n\nLa cage d'escalier du 15 rue des Lilas est vraiment défraîchie. J'ai demandé un devis à Girard (celui qui fait le ravalement du Clos Fleuri).\n\n- Lessivage + 2 couches peinture (RDC au 5ème) : 3 200€ HT\n- Peinture plafonds paliers : 1 100€ HT\n- Remplacement rampe abîmée 2ème étage : 450€ HT\n\nTotal : 4 750€ HT soit 5 225€ TTC\n\nDurée : 1 semaine\nDisponibilité : février 2026\n\nJe transmets à Delacroix ?\n\nThomas\n\n---\n📎 Pièce jointe : devis_peinture_15lilas.pdf (123 Ko)",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Sophie Marchand",
            "from_email": "s.marchand@elron-gestion.fr",
            "subject": "Re: Devis peinture cage d'escalier - 15 rue des Lilas",
            "body": "Oui envoie à Delacroix. Le montant est correct pour 6 niveaux.\n\nPar contre il faut prévenir les locataires à l'avance, la dernière fois Lambert s'était plainte de l'odeur de peinture.\n\nSophie",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Devis peinture cage d'escalier - 15 rue des Lilas",
            "body": "OK. Je demanderai à Girard d'utiliser de la peinture sans odeur (acrylique), ça évite les soucis.\n\nJe prépare un avis aux locataires dès qu'on a la date.",
            "is_reply": True,
        },
    ],
})

# === 29. NOUVEAU MANDAT DE GESTION ===
FR_STORYLINES.append({
    "id": "nouveau_mandat_gestion",
    "thread_subject": "Demande de prise en gestion - Immeuble 9 rue Pasteur, Lyon",
    "emails": [
        {
            "archived": False,
            "from_name": "Françoise Lemaire",
            "from_email": "f.lemaire.immo@gmail.com",
            "subject": "Demande de prise en gestion - Immeuble 9 rue Pasteur, Lyon",
            "body": "Madame Marchand,\n\nJe suis propriétaire d'un immeuble de 6 lots situé au 9 rue Pasteur à Lyon (3 T2 + 2 T3 + 1 local commercial). L'immeuble est actuellement géré par une autre agence mais je ne suis pas satisfaite de leurs prestations.\n\nJe souhaiterais vous rencontrer pour discuter d'un éventuel mandat de gestion. Pourriez-vous me proposer un rendez-vous ?\n\nQuelques informations :\n- Année de construction : 1975\n- DPE moyen : D\n- Tous les lots sont occupés\n- Loyers mensuels totaux : environ 4 800€\n- Pas d'impayés actuellement\n\nCordialement,\nFrançoise Lemaire\n06 XX XX XX XX",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Sophie Marchand",
            "from_email": "s.marchand@elron-gestion.fr",
            "subject": "Re: Demande de prise en gestion - Immeuble 9 rue Pasteur, Lyon",
            "body": "Bonjour Mme Lemaire,\n\nMerci pour votre prise de contact. Votre immeuble correspond tout à fait à notre domaine de compétence.\n\nJe serais ravie de vous recevoir pour en discuter. Êtes-vous disponible la semaine prochaine ? Je vous propose :\n- Mardi 14h\n- Mercredi 10h\n- Jeudi 16h\n\nJe vous préparerai notre plaquette tarifaire et les conditions de nos mandats de gestion.\n\nCordialement,\nSophie Marchand\nDirectrice d'agence - Elron Gestion",
            "is_reply": True,
        },
    ],
})

# === 30. PLAINTE ODEURS CUISINE — Mme Martin ===
FR_STORYLINES.append({
    "id": "odeurs_cuisine_martin",
    "thread_subject": "Odeurs de cuisine insupportables - 8 av Foch Apt 2A",
    "emails": [
        {
            "archived": True,
            "from_name": "Isabelle Martin",
            "from_email": "i.martin.locataire@gmail.com",
            "subject": "Odeurs de cuisine insupportables - 8 av Foch Apt 2A",
            "body": "Bonjour,\n\nJe suis désolée de vous déranger encore mais j'ai un gros problème d'odeurs de cuisine qui viennent de l'appartement voisin. Ça sent la friture en permanence, surtout le soir entre 18h et 21h.\n\nL'odeur passe par la VMC et ça imprègne tout mon appartement. J'ai essayé d'en parler à mon voisin mais il ne parle pas très bien français et n'a pas compris.\n\nEst-ce que vous pouvez intervenir ?\n\nMerci,\nI. Martin\nApt 2A",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Alexandre Morel",
            "from_email": "relaylegacy@gmail.com",
            "subject": "Re: Odeurs de cuisine insupportables - 8 av Foch Apt 2A",
            "body": "Bonjour Mme Martin,\n\nJ'ai bien noté votre plainte. Le problème vient probablement de la VMC qui mélange les flux des différents appartements. C'est un défaut courant dans les immeubles de cette époque.\n\nJe vais :\n1. Faire vérifier le système de VMC par un professionnel\n2. Envoyer un courrier de rappel au locataire concerné sur les usages (hotte aspirante, aération)\n\nEn attendant, je vous conseille de vérifier que vos bouches d'aération ne sont pas obstruées.\n\nCordialement,\nAlexandre Morel",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Isabelle Martin",
            "from_email": "i.martin.locataire@gmail.com",
            "subject": "Re: Odeurs de cuisine insupportables - 8 av Foch Apt 2A",
            "body": "Merci pour la réponse rapide.\n\nPar contre c'est pas juste un problème d'odeur de temps en temps hein. Hier soir c'était IRRESPIRABLE. J'ai dû ouvrir les fenêtres alors qu'il faisait 2 degrés dehors. Mes vêtements dans le dressing sentent la friture.\n\nJ'espère que la vérification VMC sera rapide parce que là c'est vraiment pas vivable.\n\nI. Martin",
            "is_reply": True,
        },
    ],
})

# === 31. PORTE DE GARAGE EN PANNE — Rés. Les Tilleuls ===
FR_STORYLINES.append({
    "id": "porte_garage_tilleuls",
    "thread_subject": "Porte parking automatique en panne - Rés. Les Tilleuls",
    "emails": [
        {
            "archived": True,
            "from_name": "Olivier Mercier",
            "from_email": "o.mercier.loc@gmail.com",
            "subject": "Porte parking automatique en panne - Rés. Les Tilleuls",
            "body": "Bonjour,\n\nLa porte automatique du parking souterrain de la résidence Les Tilleuls ne fonctionne plus. Elle reste bloquée en position ouverte depuis ce matin.\n\nRésultat : n'importe qui peut entrer dans le parking. C'est un problème de sécurité, surtout la nuit.\n\nMerci de faire le nécessaire.\n\nO. Mercier\nApt 5B",
            "is_reply": False,
        },
        {
            "archived": True,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Porte parking automatique en panne - Rés. Les Tilleuls",
            "body": "Bonjour M. Mercier,\n\nMerci du signalement. J'ai appelé le prestataire de maintenance (la société qui a installé le système). Un technicien devrait passer dans la journée.\n\nEn attendant, j'ai demandé au gardien de surveiller l'accès au parking.\n\nCordialement,\nThomas Lefèvre",
            "is_reply": True,
        },
        {
            "archived": True,
            "from_name": "Serrures Express",
            "from_email": "contact@serrures-express.fr",
            "subject": "Intervention porte automatique parking - Rés. Les Tilleuls",
            "body": "Bonjour M. Lefèvre,\n\nIntervention réalisée ce jour sur la porte automatique du parking de la Résidence Les Tilleuls.\n\nPanne identifiée : moteur du rideau métallique bloqué (condensateur HS). Remplacement effectué.\n\nCependant, le système de télécommande montre des signes de fatigue (récepteur intermittent). Je recommande un remplacement préventif du boîtier récepteur pour éviter une nouvelle panne à court terme.\n\nDevis complémentaire :\n- Boîtier récepteur Nice FLOX2 : 185€ HT\n- Programmation 24 télécommandes : 120€ HT\n- Main d'œuvre : 80€ HT\nTotal TTC : 462€\n\nFacture intervention du jour :\n- Condensateur moteur : 45€ HT\n- Main d'œuvre (1h30) : 95€ HT\nTotal TTC : 168€\n\nCordialement,\nSerrures Express\n\n---\n📎 Pièce jointe : facture_SE-2026-0034.pdf (67 Ko)\n📎 Pièce jointe : devis_SE-2026-0035.pdf (54 Ko)",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Patrick Leroy",
            "from_email": "p.leroy.locataire@gmail.com",
            "subject": "Re: Porte parking automatique en panne - Rés. Les Tilleuls",
            "body": "Bonjour,\n\nLa porte du parking remarche depuis hier, merci. Par contre ma télécommande ne fonctionne qu'une fois sur deux. Il faut appuyer 3-4 fois avant que ça s'ouvre.\n\nD'autres voisins ont le même problème ?\n\nP. Leroy",
            "is_reply": True,
        },
    ],
})

# ---------------------------------------------------------------------------
# STANDALONE EMAILS — ARCHIVED
# ---------------------------------------------------------------------------
FR_STANDALONE_ARCHIVED = [
    # --- Confirmations de loyer ---
    {
        "from_name": "Marc Dupont",
        "from_email": "m.dupont.locataire@gmail.com",
        "subject": "Virement loyer décembre effectué",
        "body": "Bonjour,\n\nJe vous confirme le virement du loyer de décembre (1 300€ charges comprises).\n\nCordialement,\nM. Dupont",
    },
    {
        "from_name": "Fatima Bouzid",
        "from_email": "f.bouzid.loc@gmail.com",
        "subject": "Loyer janvier - virement fait",
        "body": "Bonjour, virement du loyer de janvier fait ce matin (680€). Bonne journée. F. Bouzid",
    },
    {
        "from_name": "Catherine Moreau",
        "from_email": "c.moreau.loc@gmail.com",
        "subject": "Confirmation paiement loyer",
        "body": "Bonjour\n\nLoyer de novembre payé par virement comme d'habitude.\n\nC. Moreau",
    },
    {
        "from_name": "Nicolas Roux",
        "from_email": "n.roux.tenant@gmail.com",
        "subject": "Loyer décembre OK",
        "body": "Bonjour,\n\nVirement effectué pour le loyer de décembre (595€).\n\nBien cordialement,\nNicolas Roux",
    },
    {
        "from_name": "Émilie Garnier",
        "from_email": "e.garnier.loc@gmail.com",
        "subject": "Paiement loyer novembre",
        "body": "bonsoir\n\nje viens de faire le virement pour le loyer de novembre. Désolée pour les 2 jours de retard, problème avec ma banque.\n\nEmilie",
    },
    {
        "from_name": "Hélène Fournier",
        "from_email": "h.fournier.loc@gmail.com",
        "subject": "Loyer décembre viré",
        "body": "Bonjour Mme Hamdi,\n\nJe vous informe que le virement du loyer de décembre a été effectué ce jour.\n\nCordialement,\nHélène Fournier\nRés. Le Clos Fleuri - Apt 2A",
    },
    {
        "from_name": "Youssef El Amrani",
        "from_email": "y.elamrani.loc@gmail.com",
        "subject": "Loyer octobre envoyé",
        "body": "Bonjour\n\nVirement fait pour octobre. 720 euros comme d'hab.\n\nY. El Amrani",
    },
    # --- Demandes de quittance ---
    {
        "from_name": "Tran Nguyen",
        "from_email": "t.nguyen.loc@gmail.com",
        "subject": "Demande quittance de loyer octobre et novembre",
        "body": "Bonjour,\n\nPourriez-vous m'envoyer les quittances de loyer pour les mois d'octobre et novembre 2025 ? J'en ai besoin pour un dossier CAF.\n\nMerci d'avance,\nTran Nguyen",
    },
    {
        "from_name": "Amina Diallo",
        "from_email": "a.diallo.loc@gmail.com",
        "subject": "quittances svp",
        "body": "bonjour\n\nest ce que vous pouvez menvoyer les quittances de septembre octobre novembre decembre svp ? c'est pour la CAF ils me les demandent pour le renouvellement APL.\n\nmerci beaucoup\namina diallo",
    },
    {
        "from_name": "Antonio Rodriguez",
        "from_email": "a.rodriguez.tenant@gmail.com",
        "subject": "Attestation de domicile + quittances",
        "body": "Bonjour,\n\nDans le cadre de mon déménagement, j'aurais besoin :\n1. D'une attestation de domicile\n2. Des quittances de loyer des 6 derniers mois\n\nPourriez-vous me les envoyer par mail ?\n\nMerci,\nA. Rodriguez",
    },
    # --- Messages internes courts ---
    {
        "from_name": "Thomas Lefèvre",
        "from_email": "t.lefevre@elron-gestion.fr",
        "subject": "Clés local technique Tilleuls",
        "body": "Nadia,\n\nTu sais où sont les doubles des clés du local technique des Tilleuls ? J'ai perdu mon trousseau quelque part.\n\nThomas",
    },
    {
        "from_name": "Nadia Hamdi",
        "from_email": "n.hamdi@elron-gestion.fr",
        "subject": "Re: Clés local technique Tilleuls",
        "body": "Dans le tiroir du haut de l'armoire métallique, enveloppe marquée \"Tilleuls\".\n\nNadia",
    },
    {
        "from_name": "Julie Renard",
        "from_email": "j.renard@elron-gestion.fr",
        "subject": "Rappel : provisions propriétaires Q4",
        "body": "Bonjour Sophie,\n\nPlusieurs propriétaires n'ont pas encore versé leur provision pour charges Q4 :\n- M. Delacroix (15 rue des Lilas) : 1 200€\n- SCI Les Platanes (23 rue Voltaire) : 850€\n- M. Blanchard (17 rue du Marché) : 600€\n\nJe relance par courrier ou tu préfères les appeler ?\n\nJulie",
    },
    {
        "from_name": "Sophie Marchand",
        "from_email": "s.marchand@elron-gestion.fr",
        "subject": "Nouveau logiciel - formation le 20/01",
        "body": "Bonjour à tous,\n\nRappel : la formation sur le nouveau logiciel de gestion locative est programmée le 20 janvier de 9h à 12h. Le formateur viendra dans nos locaux.\n\nMerci de bloquer le créneau.\n\nSophie",
    },
    {
        "from_name": "Alexandre Morel",
        "from_email": "relaylegacy@gmail.com",
        "subject": "Visite appart vacant 17 rue du Marché",
        "body": "Nadia,\n\nJ'ai 3 visites programmées pour le T2 au 17 rue du Marché (apt 2B, celui de Roux qui part fin janvier) :\n- Samedi 10h : Mme Bertrand (infirmière CHU)\n- Samedi 11h : M. et Mme Charpentier (enseignants)\n- Samedi 14h : M. Koné (ingénieur)\n\nTu peux me préparer les clés et les fiches de visite stp ?\n\nAlexandre",
    },
    {
        "from_name": "Thomas Lefèvre",
        "from_email": "t.lefevre@elron-gestion.fr",
        "subject": "Re: Rappel diagnostic amiante",
        "body": "Sophie,\n\nLe diagnostic amiante du 42 bd Gambetta expire en février. J'ai demandé un RDV à ABC Diagnostics, ils peuvent venir le 5 février.\n\nCoût : 350€ HT (même tarif que l'année dernière).\n\nJe valide ?\n\nThomas",
    },
    {
        "from_name": "Nadia Hamdi",
        "from_email": "n.hamdi@elron-gestion.fr",
        "subject": "Congé le 24 janvier",
        "body": "Bonjour Sophie,\n\nJe souhaitais poser un jour de congé le vendredi 24 janvier (motif personnel). Est-ce possible ?\n\nMerci,\nNadia",
    },
    {
        "from_name": "Sophie Marchand",
        "from_email": "s.marchand@elron-gestion.fr",
        "subject": "Re: Congé le 24 janvier",
        "body": "Pas de souci Nadia, c'est noté. Bon week-end prolongé !\n\nSophie",
    },
    # --- Messages propriétaires ---
    {
        "from_name": "Philippe de Villiers",
        "from_email": "p.devilliers@orange.fr",
        "subject": "Point mensuel Résidence Les Tilleuls",
        "body": "Bonjour Mme Marchand,\n\nPourriez-vous m'envoyer le point mensuel de décembre pour la résidence Les Tilleuls ? Je souhaite notamment connaître :\n- L'état des impayés\n- Le suivi de la réparation de l'ascenseur\n- Les charges exceptionnelles du mois\n\nMerci d'avance,\nPh. de Villiers",
    },
    {
        "from_name": "Marie-Claire Fontaine",
        "from_email": "mc.fontaine@sfr.fr",
        "subject": "Travaux humidité apt Dupont",
        "body": "Bonjour Alexandre,\n\nSuite à notre échange sur le renouvellement du bail Dupont, j'ai bien noté que je m'engage à faire réaliser les travaux d'humidité au printemps.\n\nPouvez-vous me faire parvenir 2-3 devis de professionnels ? Je voudrais comparer avant de choisir.\n\nMerci,\nMC Fontaine",
    },
    {
        "from_name": "SCI Les Platanes",
        "from_email": "sci.platanes@gmail.com",
        "subject": "Rendement locatif 2025 - 23 rue Voltaire",
        "body": "Madame Marchand,\n\nDans le cadre de notre bilan annuel, pourriez-vous nous communiquer le récapitulatif des revenus locatifs et charges pour l'année 2025 concernant le 23 rue Voltaire ?\n\nNous en avons besoin pour notre AG de mars.\n\nCordialement,\nJacques Morvan\nGérant - SCI Les Platanes",
    },
    {
        "from_name": "Jean-Marc Delacroix",
        "from_email": "jm.delacroix@free.fr",
        "subject": "Augmentation loyer Bouzid ?",
        "body": "Bonjour,\n\nLe bail de Mme Bouzid (apt 1B, 15 rue des Lilas) arrive à renouvellement en mars. Est-ce qu'on peut appliquer une révision de loyer ? Le loyer actuel (620€) me semble bas pour le quartier.\n\nMerci de me dire ce qui est possible légalement.\n\nJM Delacroix",
    },
    # --- Notifications admin / syndic ---
    {
        "from_name": "Cabinet Gérard & Associés",
        "from_email": "syndic@gerard-associes.fr",
        "subject": "Convocation AG extraordinaire - 42 bd Gambetta",
        "body": "Madame, Monsieur,\n\nVous êtes convoqué(e) à l'Assemblée Générale Extraordinaire de la copropriété du 42 boulevard Gambetta, Bordeaux, qui se tiendra le :\n\nDate : Jeudi 6 février 2026 à 18h30\nLieu : Salle des fêtes municipale, 12 rue de la République\n\nOrdre du jour :\n1. Approbation des comptes 2025\n2. Vote travaux ravalement façade\n3. Remplacement gardien\n4. Questions diverses\n\nVeuillez trouver ci-joint les documents préparatoires.\n\nLe Syndic\nCabinet Gérard & Associés\n\n---\n📎 Pièce jointe : convocation_AGE_42bdGambetta.pdf (234 Ko)\n📎 Pièce jointe : comptes_2025.pdf (567 Ko)\n📎 Pièce jointe : devis_ravalement.pdf (1.8 Mo)",
    },
    {
        "from_name": "MAIF Assurances",
        "from_email": "sinistres@maif.fr",
        "subject": "Dossier sinistre SIN-2025-1207-003 - Suivi",
        "body": "Bonjour,\n\nNous accusons réception de votre déclaration de sinistre dégât des eaux (réf. SIN-2025-1207-003).\n\nUn expert a été mandaté. Il prendra contact avec vous sous 10 jours ouvrés pour convenir d'un rendez-vous.\n\nVotre dossier est suivi par Mme Duchemin (poste 4523).\n\nCordialement,\nMAIF Assurances\nService Sinistres",
    },
    {
        "from_name": "DPE Express",
        "from_email": "rdv@dpe-express.fr",
        "subject": "Confirmation RDV diagnostic - 5 impasse des Acacias",
        "body": "Bonjour,\n\nNous vous confirmons le rendez-vous pour le diagnostic de performance énergétique (DPE) du logement situé au 5 impasse des Acacias, Apt 1C, Toulouse.\n\nDate : Vendredi 3 janvier 2026 à 14h00\nDurée estimée : 1h30\nDiagnostiqueur : M. Fernandez\n\nMerci de vous assurer que le logement est accessible et le chauffage en fonctionnement.\n\nCordialement,\nDPE Express",
    },
    # --- Emails prestataires ---
    {
        "from_name": "ProNet Services",
        "from_email": "commercial@pronet-services.fr",
        "subject": "Renouvellement contrat nettoyage 2026",
        "body": "Bonjour Mme Marchand,\n\nLe contrat de nettoyage des parties communes pour la Résidence Les Tilleuls et le Clos Fleuri arrive à échéance le 31/01/2026.\n\nNous vous proposons le renouvellement aux conditions suivantes :\n\n- Résidence Les Tilleuls : 420€ HT/mois (contre 400€ en 2025, +5%)\n  → 2 passages/semaine, escaliers + hall + local poubelles\n\n- Résidence Le Clos Fleuri : 380€ HT/mois (contre 360€ en 2025, +5.5%)\n  → 2 passages/semaine, escaliers + hall + parking\n\nL'augmentation reflète la hausse du SMIC et des produits d'entretien.\n\nMerci de nous faire part de votre décision avant le 15 janvier.\n\nCordialement,\nSophie Morin\nProNet Services\n\n---\n📎 Pièce jointe : proposition_contrat_2026_ProNet.pdf (178 Ko)",
    },
    {
        "from_name": "Jardins Méditerranée",
        "from_email": "contact@jardins-med.fr",
        "subject": "Devis entretien espaces verts - Rés. Le Clos Fleuri",
        "body": "Bonjour,\n\nSuite à notre visite du 15 décembre, voici notre devis pour l'entretien annuel des espaces verts de la Résidence Le Clos Fleuri :\n\n- Tonte pelouse (mars-octobre, 2x/mois) : 1 800€ HT/an\n- Taille haies et arbustes (2x/an) : 600€ HT\n- Désherbage allées (4x/an) : 400€ HT\n- Ramassage feuilles automne : 300€ HT\n\nTotal annuel HT : 3 100,00 €\nTVA 20% : 620,00 €\nTotal TTC : 3 720,00 €\n\nDevis valable 2 mois.\n\nCordialement,\nJardins Méditerranée\n\n---\n📎 Pièce jointe : devis_JM-2025-0412.pdf (89 Ko)",
    },
    {
        "from_name": "Elec+ Électricité",
        "from_email": "devis@elecplus.fr",
        "subject": "Devis remplacement tableau électrique - 15 rue des Lilas",
        "body": "Bonjour M. Lefèvre,\n\nSuite à notre diagnostic du 12/12, le tableau électrique de l'appartement 1B au 15 rue des Lilas n'est pas aux normes (pas de différentiel 30mA, fusibles au lieu de disjoncteurs).\n\nDevis remplacement complet :\n- Tableau 2 rangées 13 modules : 185€ HT\n- Disjoncteurs + différentiels : 340€ HT\n- Main d'œuvre (1 journée) : 380€ HT\n- Mise en conformité + Consuel : 150€ HT\n\nTotal HT : 1 055,00 €\nTVA 10% : 105,50 €\nTotal TTC : 1 160,50 €\n\nDurée : 1 journée\nDisponibilité : à partir du 6 janvier\n\nCordialement,\nElec+\n\n---\n📎 Pièce jointe : devis_EP-2025-0723.pdf (67 Ko)",
    },
    # --- Spam / newsletters ---
    {
        "from_name": "Nexity Immobilier",
        "from_email": "newsletter@nexity.fr",
        "subject": "Les tendances du marché immobilier 2026 - Newsletter Nexity",
        "body": "Bonjour,\n\nDécouvrez notre analyse des tendances du marché immobilier pour 2026 :\n\n▸ Prix au m² : stabilisation attendue dans les grandes métropoles\n▸ Taux d'intérêt : légère baisse prévue au S2 2026\n▸ Location : tension persistante dans les centres-villes\n▸ Rénovation énergétique : nouvelles obligations DPE\n\nLire l'article complet ↓\n\n---\nSe désinscrire : https://nexity.fr/unsubscribe",
    },
    {
        "from_name": "Logiciel GestionFacile",
        "from_email": "commercial@gestionfacile.fr",
        "subject": "Simplifiez votre gestion locative avec GestionFacile Pro !",
        "body": "Bonjour,\n\nVous gérez un parc immobilier ? GestionFacile Pro vous fait gagner 10h/semaine :\n\n✅ Quittances automatiques\n✅ Suivi des impayés en temps réel\n✅ Gestion des travaux et prestataires\n✅ Déclaration fiscale simplifiée\n\nEssai gratuit 30 jours → www.gestionfacile.fr/essai\n\nÀ bientôt,\nL'équipe GestionFacile",
    },
    {
        "from_name": "Formation Immobilier Pro",
        "from_email": "info@formation-immo-pro.fr",
        "subject": "Formation : Loi Climat et Résilience - Impact sur la gestion locative",
        "body": "Cher(e) professionnel(le),\n\nNouvelle formation en ligne disponible :\n\n\"Loi Climat et Résilience : ce qui change pour les gestionnaires locatifs en 2026\"\n\n- Interdiction de location des passoires thermiques (DPE G)\n- Nouvelles obligations de rénovation\n- Audit énergétique obligatoire\n- Sanctions et calendrier\n\nDurée : 3h | En ligne | 290€ HT\n\nInscription : www.formation-immo-pro.fr/climat2026",
    },
    {
        "from_name": "Allianz Assurance PNO",
        "from_email": "partenaires@allianz.fr",
        "subject": "Offre spéciale assurance Propriétaire Non Occupant",
        "body": "Bonjour,\n\nEn tant que gestionnaire immobilier, bénéficiez de tarifs préférentiels sur l'assurance PNO Allianz :\n\n- À partir de 8€/mois par lot\n- Garantie loyers impayés incluse\n- Protection juridique\n\nDemandez votre devis personnalisé.\n\n---\nAllianz France - Service Partenaires",
    },
    # --- Emails assurance / juridique ---
    {
        "from_name": "Cabinet Maitre Duval",
        "from_email": "secretariat@duval-avocat.fr",
        "subject": "Dossier contentieux Garnier - Commandement de payer",
        "body": "Madame Marchand,\n\nSuite à votre instruction, nous avons fait délivrer le commandement de payer à Mme Garnier (Rés. Le Clos Fleuri, Apt 4D) par voie d'huissier le 10 décembre 2025.\n\nMontant réclamé : 2 160€ (3 mois d'impayés : sept., oct., nov. 2025)\n\nMme Garnier dispose d'un délai de 2 mois pour régulariser. À défaut, nous assignerons devant le tribunal judiciaire.\n\nJe reste à votre disposition.\n\nMaître P. Duval\nAvocat au Barreau de Bordeaux\n\n---\n📎 Pièce jointe : copie_commandement_payer_garnier.pdf (345 Ko)",
    },
    {
        "from_name": "Groupama Assurances",
        "from_email": "mr.sinistres@groupama.fr",
        "subject": "Expertise dégât des eaux - 8 avenue Foch - Convocation",
        "body": "Bonjour,\n\nNous vous informons que l'expertise contradictoire concernant le sinistre dégât des eaux au 8 avenue Foch (réf. SIN-2025-1207-003) est fixée au :\n\nDate : Mardi 7 janvier 2026 à 10h00\nLieu : 8 avenue Foch, Apt 2A, Boulogne-Billancourt\n\nExpert mandaté : M. Bernard Leclercq, Cabinet Saretec\n\nMerci de vous assurer que l'accès au logement sera possible.\n\nCordialement,\nGroupama - Service Sinistres",
    },
    # --- Références à des threads existants (standalone) ---
    {
        "from_name": "Thomas Lefèvre",
        "from_email": "t.lefevre@elron-gestion.fr",
        "subject": "Ascenseur Tilleuls - pièce reçue, intervention lundi",
        "body": "Alexandre,\n\nBonne nouvelle : la carte électronique pour l'ascenseur des Tilleuls est arrivée. Azur Ascenseurs viendra la poser lundi matin.\n\nTu peux prévenir M. Leroy (il m'envoie un mail par jour depuis 2 semaines...) ?\n\nThomas",
    },
    {
        "from_name": "Julie Renard",
        "from_email": "j.renard@elron-gestion.fr",
        "subject": "Suite dossier Benamara - virement reçu",
        "body": "Bonjour Alexandre,\n\nInfo : j'ai bien reçu le virement de 400€ de M. Benamara. Le plan d'apurement est respecté pour l'instant.\n\nReste dû : 320€ avant le 20 décembre.\n\nJulie",
    },
    {
        "from_name": "Alexandre Morel",
        "from_email": "relaylegacy@gmail.com",
        "subject": "EDL Rodriguez - retenue sur caution",
        "body": "Sophie,\n\nSuite à l'état des lieux de sortie de M. Rodriguez (5 impasse des Acacias), voici les retenues que je propose :\n\n- Trous non rebouchés dans les murs : 80€\n- Tache de brûlure plan de travail cuisine : 150€\n- Nettoyage insuffisant : 120€\n\nTotal retenues : 350€ sur 650€ de caution\nRemboursement : 300€\n\nTu valides ?\n\nAlexandre\n\n---\n📎 Pièce jointe : EDL_sortie_rodriguez_photos.pdf (2.3 Mo)",
    },
    {
        "from_name": "Nadia Hamdi",
        "from_email": "n.hamdi@elron-gestion.fr",
        "subject": "Re: Nuisances Lambert - courrier AR envoyé",
        "body": "Alexandre,\n\nLe courrier recommandé pour Mme Petit (nuisances sonores signalées par Mme Lambert) a été envoyé. AR en pièce jointe.\n\nNadia\n\n---\n📎 Pièce jointe : AR_courrier_petit_nuisances.pdf (23 Ko)",
    },
    # --- Emails divers ---
    {
        "from_name": "Marie Petit",
        "from_email": "m.petit.locataire@gmail.com",
        "subject": "Problème interphone",
        "body": "Bonjour,\n\nMon interphone ne fonctionne plus depuis 2 jours. Les visiteurs ne peuvent plus sonner chez moi. Est-ce que c'est un problème général ou juste mon appartement ?\n\nMerci,\nMarie Petit\nApt 3B, 15 rue des Lilas",
    },
    {
        "from_name": "Olivier Mercier",
        "from_email": "o.mercier.loc@gmail.com",
        "subject": "Autorisation travaux salle de bain",
        "body": "Bonjour,\n\nJe souhaiterais refaire le carrelage de ma salle de bain à mes frais. C'est possible ? Il faut une autorisation écrite ?\n\nMerci,\nO. Mercier\nApt 5B, Rés. Les Tilleuls",
    },
    {
        "from_name": "SCI Garonne Patrimoine",
        "from_email": "contact@garonne-patrimoine.fr",
        "subject": "Planning visites janvier - Toulouse",
        "body": "Bonjour M. Morel,\n\nSuite au départ de M. Rodriguez, merci de lancer les annonces pour le T3 au 5 impasse des Acacias dès que les travaux de remise en état seront terminés.\n\nBudget remise en état : max 2 000€\nLoyer cible : 750€/mois CC\n\nMerci de nous tenir informés.\n\nCordialement,\nSCI Garonne Patrimoine",
    },
    {
        "from_name": "Patrick Leroy",
        "from_email": "p.leroy.locataire@gmail.com",
        "subject": "Re: Ascenseur en panne - Résidence Les Tilleuls",
        "body": "Bonjour,\n\nMerci pour l'info. Mais ça fait quand même bientôt 2 semaines que l'ascenseur est en panne. C'est très long. Je monte 6 étages à pied tous les jours, à 73 ans c'est pas facile.\n\nY'a pas moyen d'accélérer ?\n\nP. Leroy",
    },
    {
        "from_name": "André Blanchard",
        "from_email": "a.blanchard.immo@gmail.com",
        "subject": "Taxe foncière 2025 - 17 rue du Marché",
        "body": "Bonjour Mme Renard,\n\nJ'ai reçu la taxe foncière 2025 pour le 17 rue du Marché. Montant : 1 847€.\n\nJe vous fais le virement cette semaine. Merci de noter le paiement quand vous le recevez.\n\nA. Blanchard",
    },
    {
        "from_name": "Nicolas Roux",
        "from_email": "n.roux.tenant@gmail.com",
        "subject": "Préavis de départ - N. Roux - 17 rue du Marché Apt 2B",
        "body": "Bonjour,\n\nJe vous informe de mon départ de l'appartement au 17 rue du Marché, Apt 2B.\n\nMa date de sortie souhaitée : 31 janvier 2026 (préavis d'un mois, zone tendue).\n\nJe suis muté professionnellement à Rennes.\n\nCordialement,\nNicolas Roux\n\n---\n📎 Pièce jointe : lettre_preavis_roux.pdf (34 Ko)\n📎 Pièce jointe : attestation_mutation.pdf (67 Ko)",
    },
    # --- Confirmations de loyer supplémentaires ---
    {
        "from_name": "Jean-Pierre Dubois",
        "from_email": "jp.dubois.loc@gmail.com",
        "subject": "Loyer janvier viré",
        "body": "Bonjour,\n\nVirement effectué pour le loyer de janvier (890€ CC).\n\nCordialement,\nJP Dubois\nApt 5B, 42 bd Gambetta",
    },
    {
        "from_name": "Tran Nguyen",
        "from_email": "t.nguyen.loc@gmail.com",
        "subject": "Virement loyer décembre",
        "body": "Bonjour,\n\nvirement du loyer de décembre fait ce jour. 680€ comme chaque mois.\n\nBonne fin d'année,\nT. Nguyen\n23 rue Voltaire, Apt 2C",
    },
    {
        "from_name": "Christine Lambert",
        "from_email": "c.lambert.appt@gmail.com",
        "subject": "Loyer novembre payé",
        "body": "Bonjour Mme Hamdi,\n\nJe vous confirme avoir effectué le virement du loyer de novembre ce matin.\n\nCordialement,\nChristine Lambert\n15 rue des Lilas, Apt 4A",
    },
    {
        "from_name": "Amina Diallo",
        "from_email": "a.diallo.loc@gmail.com",
        "subject": "loyer décembre viré",
        "body": "bonjour\n\nloyer de décembre envoyé par virement. 650€.\n\nbonne journée\namina",
    },
    {
        "from_name": "Olivier Mercier",
        "from_email": "o.mercier.loc@gmail.com",
        "subject": "Virement loyer novembre - Mercier",
        "body": "Bonjour,\n\nLe virement du loyer de novembre a été effectué aujourd'hui (780€ charges comprises).\n\nPourriez-vous m'envoyer la quittance dès réception ?\n\nMerci,\nOlivier Mercier\nApt 5B, Rés. Les Tilleuls",
    },
    {
        "from_name": "Patrick Leroy",
        "from_email": "p.leroy.locataire@gmail.com",
        "subject": "Loyer octobre ok",
        "body": "Bonjour\n\nVirement fait pour octobre.\n\nCdt\nP. Leroy",
    },
    {
        "from_name": "Isabelle Martin",
        "from_email": "i.martin.locataire@gmail.com",
        "subject": "Confirmation virement loyer novembre",
        "body": "Bonjour,\n\nJe vous confirme le virement du loyer de novembre (1 150€ charges comprises). Veuillez excuser le retard de 2 jours, problème technique avec ma banque en ligne.\n\nCordialement,\nIsabelle Martin\n8 avenue Foch, Apt 2A",
    },
    {
        "from_name": "Nathalie Simon",
        "from_email": "n.simon.loc@gmail.com",
        "subject": "loyer octobre viré",
        "body": "bonsoir\n\nje viens de faire le virement pour le loyer d'octobre, 620€.\n\nmerci\nnathalie simon",
    },
    # --- Messages internes supplémentaires ---
    {
        "from_name": "Julie Renard",
        "from_email": "j.renard@elron-gestion.fr",
        "subject": "Trésorerie fin d'année - recap",
        "body": "Sophie,\n\nVoici le point trésorerie au 31/12 :\n\n- Encaissements loyers décembre : 14 230€ (sur 15 680€ attendus)\n- Impayés restants : Garnier (720€) + solde Benamara (320€)\n- Charges à payer Q1 2026 : ~8 500€\n- Provisions propriétaires reçues : 3 650€ sur 5 200€ demandés\n\nOn est un peu justes sur la tréso, il faudrait relancer les provisions manquantes rapidement.\n\nJulie\n\n---\n📎 Pièce jointe : tableau_tresorerie_dec2025.xlsx (78 Ko)",
    },
    {
        "from_name": "Thomas Lefèvre",
        "from_email": "t.lefevre@elron-gestion.fr",
        "subject": "Retour visite 5 impasse des Acacias",
        "body": "Alexandre,\n\nJ'ai fait la visite de l'appart de Rodriguez après son départ. C'est globalement correct mais il y a :\n- Les trous dans les murs dont on a parlé\n- Le plan de travail abîmé\n- La salle de bain à nettoyer en profondeur\n- 2 prises électriques à refixer\n\nRien de catastrophique, un coup de peinture et du ménage et c'est bon.\n\nJe chiffre la remise en état demain.\n\nThomas",
    },
    {
        "from_name": "Nadia Hamdi",
        "from_email": "n.hamdi@elron-gestion.fr",
        "subject": "Courriers recommandés envoyés cette semaine",
        "body": "Bonjour,\n\nRécap des AR envoyés cette semaine :\n- Mme Garnier : mise en demeure loyers (fait)\n- M. Roux : relance assurance habitation (fait)\n- M. Benamara : échéancier signé (retour accusé réception)\n- Mme Lambert : réponse nuisances (fait)\n\nTout est classé dans le dossier papier + scan numérique.\n\nNadia",
    },
    {
        "from_name": "Alexandre Morel",
        "from_email": "relaylegacy@gmail.com",
        "subject": "Absence vendredi après-midi",
        "body": "Salut Thomas,\n\nJe serai absent vendredi aprèm (RDV médical). Nadia prend le relais sur les urgences.\n\nSi le propriétaire Blanchard rappelle pour le diagnostic, dis-lui que c'est en cours.\n\nAlexandre",
    },
    {
        "from_name": "Sophie Marchand",
        "from_email": "s.marchand@elron-gestion.fr",
        "subject": "Réunion équipe lundi 9h - ne pas oublier",
        "body": "Rappel : réunion d'équipe lundi 9h.\n\nMerci de préparer vos points respectifs. Thomas, ramène les devis chaudière. Julie, le point tréso. Alexandre, les dossiers relocation en cours.\n\nSophie",
    },
    # --- Communications propriétaires supplémentaires ---
    {
        "from_name": "Jean-Marc Delacroix",
        "from_email": "jm.delacroix@free.fr",
        "subject": "Déclaration revenus fonciers 2025",
        "body": "Bonjour Mme Renard,\n\nPour ma déclaration de revenus fonciers 2025, pourriez-vous me préparer :\n- Le récapitulatif des loyers encaissés\n- Le détail des charges déductibles\n- Les factures de travaux (plomberie Apt 3B notamment)\n\nJ'en aurais besoin pour fin février si possible.\n\nMerci,\nJM Delacroix",
    },
    {
        "from_name": "SCI Garonne Patrimoine",
        "from_email": "contact@garonne-patrimoine.fr",
        "subject": "Revalorisation loyer El Amrani",
        "body": "Bonjour,\n\nLe bail de M. El Amrani (5 impasse des Acacias, Apt 3B) arrive à échéance en avril. Nous souhaitons appliquer la révision selon l'IRL.\n\nLoyer actuel : 720€\nIRL de référence : T3 2025\n\nMerci de calculer le nouveau loyer et de préparer l'avenant.\n\nCordialement,\nSCI Garonne Patrimoine",
    },
    {
        "from_name": "Marie-Claire Fontaine",
        "from_email": "mc.fontaine@sfr.fr",
        "subject": "Rendement 2025 - question",
        "body": "Bonjour,\n\nPouvez-vous me dire quel a été le rendement net de mon bien au 8 avenue Foch en 2025 ? Avec le dégât des eaux et les travaux d'humidité prévus, j'ai l'impression que ça grignote la rentabilité.\n\nMerci de me faire un récap.\n\nMC Fontaine",
    },
    {
        "from_name": "Philippe de Villiers",
        "from_email": "p.devilliers@orange.fr",
        "subject": "Travaux chaudière - accord pour De Dietrich",
        "body": "Bonjour Mme Marchand,\n\nComme convenu par téléphone, je donne mon accord pour le remplacement de la chaudière par le modèle De Dietrich (devis n°2, 11 500€ TTC).\n\nMerci de programmer l'intervention pour mars, après la période de grand froid.\n\nCdt,\nPh. de Villiers",
    },
    {
        "from_name": "André Blanchard",
        "from_email": "a.blanchard.immo@gmail.com",
        "subject": "Question assurance PNO",
        "body": "Bonjour,\n\nMon assurance PNO arrive à renouvellement. Vous avez des contacts pour un bon rapport qualité/prix ? L'an dernier j'ai payé 320€ pour le 17 rue du Marché, ça me semble cher.\n\nMerci pour vos conseils.\n\nA. Blanchard",
    },
    # --- Factures et devis prestataires supplémentaires ---
    {
        "from_name": "ProNet Services",
        "from_email": "commercial@pronet-services.fr",
        "subject": "Facture nettoyage décembre 2025",
        "body": "Bonjour,\n\nVeuillez trouver ci-joint nos factures de nettoyage pour décembre 2025 :\n\n- Rés. Les Tilleuls : 400,00€ HT\n- Rés. Le Clos Fleuri : 360,00€ HT\n\nTotal HT : 760,00€\nTVA 20% : 152,00€\nTotal TTC : 912,00€\n\nRèglement sous 30 jours.\n\nCordialement,\nProNet Services\n\n---\n📎 Pièce jointe : facture_PN-2025-1247.pdf (56 Ko)\n📎 Pièce jointe : facture_PN-2025-1248.pdf (54 Ko)",
    },
    {
        "from_name": "SOS Nuisibles",
        "from_email": "intervention@sos-nuisibles.fr",
        "subject": "Rapport intervention cafards - 17 rue du Marché",
        "body": "Bonjour,\n\nSuite à notre intervention du 05/12 au 17 rue du Marché, Apt 1A :\n\n- Traitement gel insecticide appliqué (cuisine, salle de bain, gaines techniques)\n- Présence confirmée : blattes germaniques, infestation modérée\n- Visite de contrôle prévue J+21\n\nRecommandations :\n- Colmater les passages autour des tuyaux dans la cuisine\n- Vérifier les appartements adjacents\n\nFacture jointe : 180€ TTC\n\nCordialement,\nSOS Nuisibles\n\n---\n📎 Pièce jointe : rapport_intervention_SOS_171225.pdf (234 Ko)\n📎 Pièce jointe : facture_SOS-2025-0892.pdf (45 Ko)",
    },
    {
        "from_name": "Toitures Durand",
        "from_email": "contact@toitures-durand.fr",
        "subject": "Devis réparation toiture - 42 bd Gambetta",
        "body": "Bonjour M. Lefèvre,\n\nSuite à votre demande, voici notre devis pour la réparation de la toiture du 42 bd Gambetta (fuites signalées au 5ème étage) :\n\n- Remplacement tuiles cassées (x12) : 480€ HT\n- Reprise faîtage (3 ml) : 350€ HT\n- Vérification étanchéité noue : 200€ HT\n- Échafaudage / nacelle : 600€ HT\n\nTotal HT : 1 630,00€\nTVA 10% : 163,00€\nTotal TTC : 1 793,00€\n\nDisponibilité : fin janvier 2026 (si météo OK)\n\nCordialement,\nDurand Toitures\n\n---\n📎 Pièce jointe : devis_TD-2025-0341.pdf (98 Ko)",
    },
    {
        "from_name": "Duplex Plomberie",
        "from_email": "contact@duplex-plomberie.fr",
        "subject": "Facture intervention siphon - 8 av Foch Apt 2A",
        "body": "Bonjour,\n\nFacture pour l'intervention du 08/01 au 8 avenue Foch, Apt 2A :\n- Remplacement siphon évier SDB : 35€ HT\n- Main d'œuvre (30 min) : 45€ HT\n- Déplacement : 45€ HT\n\nTotal TTC : 137,50€\n\nCordialement,\nDuplex Plomberie\n\n---\n📎 Pièce jointe : facture_FAC-2026-0012.pdf (56 Ko)",
    },
    {
        "from_name": "ABC Diagnostics",
        "from_email": "rdv@abc-diagnostics.fr",
        "subject": "Facture diagnostic amiante - 42 bd Gambetta",
        "body": "Bonjour,\n\nVeuillez trouver ci-joint la facture et le rapport de diagnostic amiante pour le 42 boulevard Gambetta.\n\nRésultat : absence d'amiante dans les matériaux analysés.\nValidité du diagnostic : 3 ans\n\nMontant : 350€ HT / 420€ TTC\n\nCordialement,\nABC Diagnostics\n\n---\n📎 Pièce jointe : facture_ABC-2026-0087.pdf (45 Ko)\n📎 Pièce jointe : rapport_amiante_42gambetta.pdf (567 Ko)",
    },
    # --- Emails admin/juridique/assurance supplémentaires ---
    {
        "from_name": "Préfecture de la Gironde",
        "from_email": "service-logement@gironde.gouv.fr",
        "subject": "Rappel obligations DPE - Interdiction location logements classés G",
        "body": "Madame, Monsieur,\n\nNous vous rappelons que depuis le 1er janvier 2025, les logements classés G au diagnostic de performance énergétique ne peuvent plus être proposés à la location en tant que résidence principale.\n\nMerci de vérifier que l'ensemble de votre parc locatif est en conformité. En cas de contrôle, des sanctions sont prévues.\n\nPour plus d'informations : www.ecologie.gouv.fr/dpe\n\nLe Service Logement\nPréfecture de la Gironde",
    },
    {
        "from_name": "MAIF Assurances",
        "from_email": "sinistres@maif.fr",
        "subject": "Dossier SIN-2025-1207-003 - Rapport expert disponible",
        "body": "Bonjour,\n\nLe rapport d'expertise relatif au sinistre dégât des eaux (réf. SIN-2025-1207-003) au 8 avenue Foch est désormais disponible.\n\nConclusion de l'expert :\n- Origine du sinistre : joint défectueux machine à laver, Apt 2B\n- Dommages Apt 2A : plafond cuisine, mur séjour, parquet entrée\n- Chiffrage des réparations : 3 450€\n\nLa prise en charge sera effectuée par l'assurance du responsable (Apt 2B).\n\nUn courrier détaillé vous sera adressé sous 15 jours.\n\nCordialement,\nMAIF - Service Sinistres\n\n---\n📎 Pièce jointe : rapport_expertise_SIN-2025-1207-003.pdf (1.8 Mo)",
    },
    {
        "from_name": "Cabinet Maitre Duval",
        "from_email": "secretariat@duval-avocat.fr",
        "subject": "Point dossier Garnier - pas de régularisation",
        "body": "Madame Marchand,\n\nLe délai de 2 mois du commandement de payer expirera le 10 février 2026. À ce jour, Mme Garnier n'a effectué aucun versement.\n\nCependant, elle nous a informés par courrier qu'elle a déposé un dossier FSL. Souhaitez-vous attendre le résultat du FSL avant d'engager la procédure d'assignation ?\n\nMerci de me donner vos instructions.\n\nCordialement,\nMaître P. Duval",
    },
    {
        "from_name": "Caisse d'Allocations Familiales",
        "from_email": "ne-pas-repondre@caf.fr",
        "subject": "Demande d'information bailleur - Dossier Diallo",
        "body": "Madame, Monsieur,\n\nDans le cadre du renouvellement de l'Aide Personnalisée au Logement de Mme Amina Diallo (allocataire n° 1234567X), nous avons besoin de l'attestation de loyer actualisée.\n\nMerci de compléter le formulaire en ligne sur caf.fr ou de nous retourner l'imprimé ci-joint dans un délai de 15 jours.\n\nService Prestations Logement\nCAF\n\n---\n📎 Pièce jointe : formulaire_attestation_loyer_CAF.pdf (123 Ko)",
    },
    {
        "from_name": "Groupama Assurances",
        "from_email": "mr.sinistres@groupama.fr",
        "subject": "Renouvellement contrat MRH immeuble - 15 rue des Lilas",
        "body": "Bonjour,\n\nVotre contrat multirisque habitation pour l'immeuble au 15 rue des Lilas arrive à échéance le 28/02/2026.\n\nProposition de renouvellement :\n- Prime annuelle : 2 340€ TTC (vs 2 180€ en 2025, +7%)\n- Franchises inchangées\n- Garantie valeur à neuf maintenue\n\nMerci de nous confirmer le renouvellement avant le 15 février.\n\nCordialement,\nGroupama\n\n---\n📎 Pièce jointe : conditions_renouvellement_15lilas.pdf (456 Ko)",
    },
    # --- Demandes locataires supplémentaires ---
    {
        "from_name": "Christine Lambert",
        "from_email": "c.lambert.appt@gmail.com",
        "subject": "Demande quittances 3ème trimestre",
        "body": "Bonjour,\n\nPourriez-vous m'envoyer mes quittances de loyer pour juillet, août et septembre 2025 ? Mon employeur me les demande pour un dossier de mutation.\n\nMerci d'avance,\nC. Lambert\nApt 4A, 15 rue des Lilas",
    },
    {
        "from_name": "Jean-Pierre Dubois",
        "from_email": "jp.dubois.loc@gmail.com",
        "subject": "Attestation d'hébergement pour ma fille",
        "body": "Bonjour,\n\nMa fille étudiante va habiter chez moi quelques mois. Est-ce que vous pouvez me fournir une attestation d'hébergement ?\n\nMerci,\nJP Dubois\n42 bd Gambetta, Apt 5B",
    },
    {
        "from_name": "Karim Benamara",
        "from_email": "k.benamara.loc@gmail.com",
        "subject": "question charges eau",
        "body": "bonjour\n\nje comprends pas les charges d'eau sur mon dernier avis. Ca a augmenté de presque 30% par rapport a l'année dernière. C'est normal ?\n\npouvez vous m'expliquer ?\n\nmerci\nk benamara",
    },
    {
        "from_name": "Hélène Fournier",
        "from_email": "h.fournier.loc@gmail.com",
        "subject": "Demande attestation de domicile",
        "body": "Bonjour,\n\nJ'aurais besoin d'une attestation de domicile pour un dossier administratif. Pourriez-vous m'en faire parvenir une par mail ?\n\nMerci beaucoup,\nH. Fournier\nRés. Le Clos Fleuri, Apt 2A",
    },
    # --- Spam/newsletters supplémentaires ---
    {
        "from_name": "FNAIM",
        "from_email": "newsletter@fnaim.fr",
        "subject": "Webinaire : Encadrement des loyers 2026 - Nouvelles zones concernées",
        "body": "Cher adhérent,\n\nLa FNAIM organise un webinaire gratuit :\n\n\"Encadrement des loyers : nouvelles villes et zones concernées en 2026\"\n\nDate : 12 février 2026, 14h-15h30\nIntervenant : Me Gauthier, avocat spécialisé droit immobilier\n\nInscription : www.fnaim.fr/webinaire-loyers-2026\n\nCordialement,\nFNAIM - Service Formation",
    },
    {
        "from_name": "EDF Pro",
        "from_email": "collectivites@edf.fr",
        "subject": "Offre énergie verte pour vos parties communes",
        "body": "Bonjour,\n\nDécouvrez notre offre Vert Électrique pour les parties communes de vos immeubles :\n\n- 100% énergie renouvelable certifiée\n- Prix fixe garanti 2 ans\n- Facturation simplifiée multi-sites\n- Conseiller dédié\n\nSimulation gratuite sur edf.fr/pro\n\nEDF Entreprises",
    },
    {
        "from_name": "Salon de l'Immobilier Lyon",
        "from_email": "inscription@salon-immo-lyon.fr",
        "subject": "Invitation professionnelle - Salon de l'Immobilier Lyon 2026",
        "body": "Madame, Monsieur,\n\nNous avons le plaisir de vous inviter au Salon de l'Immobilier de Lyon :\n\nDates : 14-16 mars 2026\nLieu : Eurexpo, Hall 4\n\nBadge professionnel gratuit avec le code : PROGEST2026\n\nAu programme : conférences, networking, innovations PropTech\n\nÀ bientôt !\nComité d'organisation",
    },
    # --- Emails divers / références à threads ---
    {
        "from_name": "Nadia Hamdi",
        "from_email": "n.hamdi@elron-gestion.fr",
        "subject": "Quittances envoyées - Nguyen et Diallo",
        "body": "Alexandre,\n\nLes quittances demandées par M. Nguyen (oct-nov) et Mme Diallo (sept à déc) ont été envoyées par mail.\n\nNadia",
    },
    {
        "from_name": "Thomas Lefèvre",
        "from_email": "t.lefevre@elron-gestion.fr",
        "subject": "Suivi fibre optique Tilleuls - réponse Orange",
        "body": "Sophie,\n\nOrange a confirmé le raccordement fibre pour la résidence Les Tilleuls. Les travaux de colonne montante démarreront le 3 mars. Durée estimée : 2 semaines.\n\nJ'afficherai un avis dans le hall.\n\nThomas",
    },
    {
        "from_name": "Alexandre Morel",
        "from_email": "relaylegacy@gmail.com",
        "subject": "Re: Planning visites janvier - Toulouse",
        "body": "Bonjour,\n\nSuite aux 3 visites de samedi, voici mon retour :\n\n- Mme Bertrand : très intéressée, dossier complet déjà déposé\n- M. et Mme Charpentier : intéressés mais veulent revoir le loyer à la baisse (750 → 700€)\n- M. Koné : a trouvé autre chose, ne donne pas suite\n\nJe recommande Mme Bertrand. On valide ?\n\nAlexandre",
    },
    {
        "from_name": "Julie Renard",
        "from_email": "j.renard@elron-gestion.fr",
        "subject": "Virement caution Rodriguez effectué",
        "body": "Alexandre,\n\nLe virement du remboursement partiel de caution de M. Rodriguez (300€) a été effectué ce jour.\n\nJulie",
    },
    {
        "from_name": "Sophie Marchand",
        "from_email": "s.marchand@elron-gestion.fr",
        "subject": "Re: Dossier impayé Garnier - point de situation",
        "body": "Bonjour,\n\nSuite au mail de la SCI et au retour de Me Duval : on accorde le délai à Mme Garnier pour le FSL, mais on maintient la pression. Si aucun versement d'ici fin février, on assigne.\n\nAlexandre, peux-tu lui écrire pour formaliser ?\n\nSophie",
    },
]

# ---------------------------------------------------------------------------
# STANDALONE EMAILS — INBOX (récents, non lus)
# ---------------------------------------------------------------------------
FR_STANDALONE_INBOX = [
    # --- Nouvelles demandes locataires ---
    {
        "from_name": "Fatima Bouzid",
        "from_email": "f.bouzid.loc@gmail.com",
        "subject": "Moisissure derrière meuble cuisine",
        "body": "bonjour\n\nen déplaçant un meuble j'ai découvert de la moisissure noire derrière, sur le mur de la cuisine. C'est assez étendu (environ 50cm x 30cm). Je pense que c'est lié à l'humidité.\n\nqu'est ce que je dois faire ?\n\nmerci\nfatima bouzid\napt 1B 15 rue des lilas",
    },
    {
        "from_name": "Youssef El Amrani",
        "from_email": "y.elamrani.loc@gmail.com",
        "subject": "Problème volet roulant bloqué",
        "body": "Bonjour,\n\nLe volet roulant de la chambre est bloqué en position fermée depuis ce matin. J'ai essayé de forcer un peu mais rien à faire, la sangle tourne dans le vide.\n\nOn est dans le noir total dans la chambre du coup.\n\nMerci d'envoyer quelqu'un.\n\nY. El Amrani\n5 impasse des Acacias, Apt 3B",
    },
    {
        "from_name": "Hélène Fournier",
        "from_email": "h.fournier.loc@gmail.com",
        "subject": "Talon de loyer non reçu",
        "body": "Bonjour,\n\nJe n'ai pas reçu mon appel de loyer pour le mois prochain. D'habitude il arrive vers le 20 du mois. On est le 22 et toujours rien.\n\nPourriez-vous vérifier ?\n\nMerci,\nH. Fournier\nRés. Le Clos Fleuri, Apt 2A",
    },
    {
        "from_name": "Jean-Pierre Dubois",
        "from_email": "jp.dubois.loc@gmail.com",
        "subject": "Re: Fissure importante mur salon - 42 bd Gambetta Apt 5B",
        "body": "Bonjour M. Lefèvre,\n\nJe voulais vous signaler que la fissure dans le salon s'est encore agrandie. Elle fait maintenant presque 60cm et elle est plus ouverte qu'avant. J'ai mis un bout de scotch en travers pour voir si ça bouge encore.\n\nC'est inquiétant, j'aimerais vraiment que l'expert vienne rapidement.\n\nMerci,\nJP Dubois",
    },
    # --- Messages internes récents ---
    {
        "from_name": "Sophie Marchand",
        "from_email": "s.marchand@elron-gestion.fr",
        "subject": "Objectifs Q1 2026 - à discuter en réunion",
        "body": "Bonjour à tous,\n\nAvant la réunion de lundi, voici les points que je souhaite aborder :\n\n1. Réduction du taux d'impayés (objectif : passer sous 3%)\n2. Relocation des logements vacants (3 lots à pourvoir)\n3. Suivi des gros travaux (ravalement Clos Fleuri, chaudière Tilleuls)\n4. Prospection nouveaux mandats\n\nMerci de préparer vos retours.\n\nSophie",
    },
    {
        "from_name": "Thomas Lefèvre",
        "from_email": "t.lefevre@elron-gestion.fr",
        "subject": "Devis chaudière neuve Tilleuls - comparatif",
        "body": "Sophie, Alexandre,\n\nJ'ai reçu 3 devis pour le remplacement de la chaudière aux Tilleuls :\n\n1. ThermoConfort : chaudière gaz condensation Viessmann → 12 800€ TTC\n2. Énergie Plus : chaudière gaz condensation De Dietrich → 11 500€ TTC\n3. Chauffage Éco : PAC air-eau Daikin → 18 200€ TTC (mais éligible MaPrimeRénov')\n\nLa PAC serait plus rentable à long terme mais l'investissement initial est lourd. Je recommande le devis 2 (De Dietrich) sauf si le propriétaire veut investir dans la PAC.\n\nOn en discute lundi ?\n\nThomas\n\n---\n📎 Pièce jointe : comparatif_devis_chaudiere_tilleuls.pdf (234 Ko)",
    },
    {
        "from_name": "Julie Renard",
        "from_email": "j.renard@elron-gestion.fr",
        "subject": "Erreur prélèvement loyer Moreau",
        "body": "Alexandre,\n\nMme Moreau (17 rue du Marché) m'appelle car elle a été prélevée 2 fois pour le loyer de janvier. Effectivement je vois un double prélèvement sur le relevé.\n\nC'est une erreur de la banque, je fais le nécessaire pour le remboursement mais il faudra environ 5 jours ouvrés.\n\nTu peux lui envoyer un mail pour la rassurer stp ?\n\nJulie",
    },
    {
        "from_name": "Nadia Hamdi",
        "from_email": "n.hamdi@elron-gestion.fr",
        "subject": "Clés appartement Rodriguez récupérées",
        "body": "Bonjour,\n\nM. Rodriguez est passé ce matin rendre les clés de l'appartement (5 impasse des Acacias, Apt 1C). J'ai tout : 2 clés porte entrée + 1 clé boîte aux lettres + 1 badge parking.\n\nLe logement est vide, on peut programmer la remise en état.\n\nNadia",
    },
    {
        "from_name": "Alexandre Morel",
        "from_email": "relaylegacy@gmail.com",
        "subject": "Candidatures appart Roux - 3 dossiers reçus",
        "body": "Sophie,\n\nJ'ai reçu 3 dossiers pour le T2 du 17 rue du Marché :\n\n1. Léa Bertrand - infirmière CHU, CDI, 2 200€ net → dossier solide\n2. M. et Mme Charpentier - enseignants, 2x CDI, 3 800€ net → très bon\n3. M. Koné - ingénieur, CDI récent (6 mois), 2 800€ net → correct mais garant nécessaire\n\nMon avis : les Charpentier sont le meilleur profil. Mme Bertrand est très bien aussi.\n\nTu veux qu'on en discute ou je peux avancer ?\n\nAlexandre",
    },
    # --- Prestataires / devis ---
    {
        "from_name": "Menuiserie Caron",
        "from_email": "atelier@menuiserie-caron.fr",
        "subject": "Devis réparation volet roulant - 5 impasse des Acacias",
        "body": "Bonjour M. Lefèvre,\n\nSuite à votre appel, voici notre devis pour la réparation du volet roulant :\n\n- Déplacement + diagnostic : 50€ HT\n- Remplacement sangle + enrouleur : 85€ HT\n- Main d'œuvre : 65€ HT\n\nTotal HT : 200€\nTVA 10% : 20€\nTotal TTC : 220€\n\nDisponibilité : sous 48h après validation.\n\nCordialement,\nMenuiserie Caron",
    },
    {
        "from_name": "ABC Diagnostics",
        "from_email": "rdv@abc-diagnostics.fr",
        "subject": "Confirmation RDV diagnostic fissure - 42 bd Gambetta",
        "body": "Bonjour,\n\nNous confirmons le rendez-vous pour l'expertise de la fissure au 42 boulevard Gambetta, Apt 5B :\n\nDate : Jeudi 30 janvier 2026 à 11h00\nExpert : Mme Fournier-Legrand\n\nMerci de prévoir l'accès au logement.\n\nCordialement,\nABC Diagnostics",
    },
    {
        "from_name": "ThermoConfort SARL",
        "from_email": "devis@thermoconfort.fr",
        "subject": "Intervention urgence chauffage - Rés. Les Tilleuls - Confirmation",
        "body": "Bonjour M. Lefèvre,\n\nNous confirmons l'intervention de notre technicien demain matin (8h30) à la Résidence Les Tilleuls pour le problème de chauffage signalé.\n\nCordialement,\nThermoConfort",
    },
    # --- Messages propriétaires récents ---
    {
        "from_name": "Philippe de Villiers",
        "from_email": "p.devilliers@orange.fr",
        "subject": "Re: Devis chaudière - Les Tilleuls",
        "body": "Bonjour,\n\nJ'ai bien reçu les devis. 18 000€ pour la PAC c'est trop pour moi en ce moment. Je suis d'accord pour le devis De Dietrich à 11 500€.\n\nOn peut programmer ça pour mars ? Je voudrais éviter de couper le chauffage en plein hiver.\n\nCdt,\nPh. de Villiers",
    },
    {
        "from_name": "SCI Clos Fleuri Invest",
        "from_email": "gestion@closfleuri-invest.fr",
        "subject": "Dossier impayé Garnier - point de situation",
        "body": "Mme Marchand,\n\nOù en est le dossier Garnier ? Le commandement de payer a été signifié en décembre, avons-nous eu un retour ?\n\nSi pas de régularisation, nous souhaitons engager la procédure d'expulsion. Merci de nous donner une mise à jour.\n\nCordialement,\nSCI Clos Fleuri Invest",
    },
    # --- Spam / newsletters récents ---
    {
        "from_name": "SeLoger Pro",
        "from_email": "pro@seloger.com",
        "subject": "Boostez vos annonces avec SeLoger Premium !",
        "body": "Bonjour,\n\nVos annonces ne performent pas assez ? Passez à SeLoger Premium :\n\n→ Visibilité x3 sur SeLoger et Logic-Immo\n→ Photos HD illimitées\n→ Statistiques détaillées\n→ Badge \"Professionnel vérifié\"\n\nOffre spéciale : -20% le 1er trimestre\n\nContactez votre conseiller : 01 XX XX XX XX\n\n---\nSe désinscrire",
    },
    # --- Divers récents ---
    {
        "from_name": "Catherine Moreau",
        "from_email": "c.moreau.loc@gmail.com",
        "subject": "Visite de contrôle cafards - date ?",
        "body": "Bonjour,\n\nLa désinsectisation a été faite il y a 3 semaines maintenant. J'en vois encore quelques-uns mais nettement moins qu'avant.\n\nLa visite de contrôle est prévue quand exactement ?\n\nMerci\nC. Moreau",
    },
    {
        "from_name": "Patrick Leroy",
        "from_email": "p.leroy.locataire@gmail.com",
        "subject": "L'ascenseur remarche !! Merci",
        "body": "Bonjour M. Lefèvre,\n\nJe voulais juste vous dire merci, l'ascenseur a été réparé ce matin et il marche parfaitement. Quel soulagement après 2 semaines à monter à pied !\n\nBonne journée,\nP. Leroy",
    },
    {
        "from_name": "Thomas Lefèvre",
        "from_email": "t.lefevre@elron-gestion.fr",
        "subject": "Planning interventions semaine prochaine",
        "body": "Bonjour à tous,\n\nVoici le planning des interventions de la semaine prochaine :\n\n- Lundi : ThermoConfort → chauffage Tilleuls (8h30)\n- Mardi : Visite contrôle cafards → 17 rue du Marché (10h)\n- Mercredi : Menuiserie Caron → volet roulant 5 impasse Acacias (14h)\n- Jeudi : ABC Diagnostics → fissure 42 bd Gambetta (11h)\n- Vendredi : DPE → 5 impasse des Acacias (14h)\n\nAlexandre, tu peux prévenir les locataires concernés ?\n\nThomas",
    },
    {
        "from_name": "Émilie Garnier",
        "from_email": "e.garnier.loc@gmail.com",
        "subject": "Demande de délai supplémentaire",
        "body": "Bonjour Mme Marchand,\n\nJ'ai bien reçu le commandement de payer de votre avocat. Je suis vraiment désolée pour cette situation.\n\nJe suis en train de constituer un dossier FSL (Fonds de Solidarité Logement) avec mon assistante sociale. Est-ce que vous pouvez attendre le résultat avant de lancer une procédure d'expulsion ? Ça devrait prendre 3-4 semaines.\n\nJe m'engage à reprendre le paiement régulier du loyer courant à partir de février.\n\nCordialement,\nÉ. Garnier",
    },
    {
        "from_name": "Sophie Marchand",
        "from_email": "s.marchand@elron-gestion.fr",
        "subject": "Fwd: Demande de délai supplémentaire",
        "body": "Alexandre, Julie,\n\nVoir le mail de Mme Garnier ci-dessous. Elle demande un délai pour monter un dossier FSL.\n\nJe suis d'avis d'accorder le délai si elle reprend le paiement courant en février. On ne gagne rien à une procédure d'expulsion qui va prendre 18 mois.\n\nAvis ?\n\nSophie",
    },
    # --- Nouvelles plaintes / demandes locataires ---
    {
        "from_name": "Marc Dupont",
        "from_email": "m.dupont.locataire@gmail.com",
        "subject": "CHAUFFAGE COLLECTIF EN PANNE - 8 av Foch",
        "body": "Bonjour,\n\nPLUS DE CHAUFFAGE depuis ce matin dans tout l'immeuble au 8 avenue Foch. Il fait 14 degrés dans l'appart. Ma femme est enceinte de 7 mois et on gèle.\n\nC'est la 3ème fois cet hiver !! Il faut faire quelque chose de DÉFINITIF.\n\nM. Dupont\nApt 2B",
    },
    {
        "from_name": "Amina Diallo",
        "from_email": "a.diallo.loc@gmail.com",
        "subject": "fuite au plafond salle de bain",
        "body": "bonjour\n\nj'ai une tache d'eau au plafond de la salle de bain qui grossit depuis 2 jours. ca commence a goutter par moments. je pense que ca vient du voisin du dessus.\n\npouvez vous venir voir svp c'est urgent\n\namina diallo apt 3A rés les tilleuls\n\n---\n📎 Pièce jointe : photo_plafond_sdb.jpg (1.4 Mo)",
    },
    {
        "from_name": "Tran Nguyen",
        "from_email": "t.nguyen.loc@gmail.com",
        "subject": "Problème pression eau chaude",
        "body": "Bonjour M. Morel,\n\nDepuis quelques jours, la pression de l'eau chaude est très faible dans mon appartement, surtout au robinet de la douche. L'eau froide fonctionne normalement.\n\nEst-ce un problème général à l'immeuble ou juste chez moi ?\n\nMerci,\nT. Nguyen\n23 rue Voltaire, Apt 2C",
    },
    # --- Messages internes urgents récents ---
    {
        "from_name": "Thomas Lefèvre",
        "from_email": "t.lefevre@elron-gestion.fr",
        "subject": "Fuite colonne montante 15 rue des Lilas",
        "body": "Sophie, Alexandre,\n\nGros problème : Mme Lambert vient d'appeler, il y a une fuite importante sur la colonne montante entre le 3ème et le 4ème étage au 15 rue des Lilas. De l'eau coule dans le couloir.\n\nJ'ai appelé Duplex Plomberie en urgence, ils arrivent dans 1h. J'ai demandé au gardien de couper l'eau en attendant.\n\nJe file sur place.\n\nThomas",
    },
    {
        "from_name": "Julie Renard",
        "from_email": "j.renard@elron-gestion.fr",
        "subject": "Loyer Benamara décembre - solde reçu",
        "body": "Bonjour,\n\nBonne nouvelle : M. Benamara a viré les 320€ restants du plan d'apurement. Le loyer de novembre est donc intégralement régularisé.\n\nReste à surveiller : le loyer de décembre (720€) dû le 5 janvier.\n\nJulie",
    },
    {
        "from_name": "Nadia Hamdi",
        "from_email": "n.hamdi@elron-gestion.fr",
        "subject": "Appel Mme Fontaine - rappeler svp",
        "body": "Alexandre,\n\nMme Fontaine (proprio 8 av Foch) a appelé 2 fois ce matin. Elle veut te parler des travaux d'humidité et du rapport d'expertise du dégât des eaux.\n\nElle a l'air assez remontée. Rappelle-la avant 17h si possible.\n\nNadia",
    },
    # --- Questions propriétaires récentes ---
    {
        "from_name": "SCI Les Platanes",
        "from_email": "sci.platanes@gmail.com",
        "subject": "Vacance locative Apt 3B - 23 rue Voltaire",
        "body": "Madame Marchand,\n\nNous avons constaté que l'appartement 3B au 23 rue Voltaire est vacant depuis 2 mois. Où en sommes-nous sur la remise en location ?\n\nLe manque à gagner est de 1 400€/mois et ce n'est plus tenable. Merci de nous donner un état des lieux de la situation et vos actions en cours.\n\nCordialement,\nJ. Morvan\nSCI Les Platanes",
    },
    {
        "from_name": "Jean-Marc Delacroix",
        "from_email": "jm.delacroix@free.fr",
        "subject": "Re: Devis peinture cage d'escalier - 15 rue des Lilas",
        "body": "Bonjour,\n\nJ'ai regardé le devis Girard pour la cage d'escalier. 5 225€ TTC, c'est OK.\n\nFaites-le programmer pour février comme prévu. Par contre je veux de la peinture lavable, pas de l'acrylique basique qui se salit en 2 ans.\n\nCdt\nJM Delacroix",
    },
    # --- Confirmations prestataires ---
    {
        "from_name": "Menuiserie Caron",
        "from_email": "atelier@menuiserie-caron.fr",
        "subject": "Confirmation intervention volet - 5 impasse des Acacias",
        "body": "Bonjour,\n\nSuite à validation du devis, nous confirmons l'intervention pour la réparation du volet roulant au 5 impasse des Acacias, Apt 3B :\n\nDate : Mercredi prochain, 14h\nDurée estimée : 1h\n\nMerci de prévenir le locataire.\n\nCordialement,\nMenuiserie Caron",
    },
    {
        "from_name": "Peinture & Ravalement Girard",
        "from_email": "devis@girard-ravalement.fr",
        "subject": "Avenant devis ravalement Clos Fleuri - reprise balcons",
        "body": "Bonjour Mme Marchand,\n\nSuite à votre demande, voici le chiffrage complémentaire pour la reprise des balcons de la Résidence Le Clos Fleuri :\n\n- Réfection étanchéité 8 balcons : 4 800€ HT\n- Peinture sol + garde-corps : 2 200€ HT\n- Remplacement 3 garde-corps rouillés : 1 800€ HT\n\nTotal avenant HT : 8 800€\nTVA 10% : 880€\nTotal TTC : 9 680€\n\nSi réalisé en même temps que le ravalement, remise de 5% sur l'ensemble.\n\nCordialement,\nP. Girard\n\n---\n📎 Pièce jointe : avenant_balcons_RAV-2025-0156b.pdf (234 Ko)",
    },
    # --- Emails divers / références à threads ---
    {
        "from_name": "Alexandre Morel",
        "from_email": "relaylegacy@gmail.com",
        "subject": "Re: Contestation plan de travail Rodriguez",
        "body": "Sophie,\n\nRodriguez conteste la retenue de 150€ pour le plan de travail (brûlure). J'ai vérifié l'EDL d'entrée : effectivement rien n'est mentionné, mais la photo d'entrée est floue sur cette zone.\n\nDans le doute, je propose de réduire à 75€ pour éviter un conflit. Ça porte le remboursement à 375€. Ton avis ?\n\nAlexandre",
    },
    {
        "from_name": "Françoise Lemaire",
        "from_email": "f.lemaire.immo@gmail.com",
        "subject": "Re: Demande de prise en gestion - Immeuble 9 rue Pasteur, Lyon",
        "body": "Bonjour Mme Marchand,\n\nMerci pour votre réactivité. Le créneau de mercredi 10h me convient parfaitement.\n\nPourriez-vous m'envoyer votre adresse exacte ?\n\nCordialement,\nF. Lemaire",
    },
    # --- Notifications récentes ---
    {
        "from_name": "Enedis",
        "from_email": "interventions@enedis.fr",
        "subject": "Intervention compteur - 5 impasse des Acacias, Apt 1C",
        "body": "Bonjour,\n\nNous vous informons qu'une intervention est programmée pour le relevé et la mise hors service du compteur électrique du logement situé au 5 impasse des Acacias, Apt 1C, Toulouse.\n\nDate : Vendredi 10 janvier 2026 entre 8h et 12h\n\nMerci de vous assurer que le compteur est accessible.\n\nCordialement,\nEnedis - Service Interventions",
    },
    {
        "from_name": "Cabinet Gérard & Associés",
        "from_email": "syndic@gerard-associes.fr",
        "subject": "PV AG extraordinaire - 42 bd Gambetta",
        "body": "Madame, Monsieur,\n\nVeuillez trouver ci-joint le procès-verbal de l'Assemblée Générale Extraordinaire du 42 boulevard Gambetta qui s'est tenue le 6 février 2026.\n\nRésolutions adoptées :\n- Approbation des comptes 2025 : adoptée à l'unanimité\n- Ravalement façade (devis Girard) : adoptée à la majorité art. 25\n- Remplacement gardien : reporté à la prochaine AG\n\nCordialement,\nLe Syndic\n\n---\n📎 Pièce jointe : PV_AGE_42bdGambetta_06022026.pdf (345 Ko)",
    },
    {
        "from_name": "DPE Express",
        "from_email": "rdv@dpe-express.fr",
        "subject": "Résultat DPE - 5 impasse des Acacias Apt 1C",
        "body": "Bonjour,\n\nSuite au diagnostic du 3 janvier, voici les résultats du DPE pour le logement au 5 impasse des Acacias, Apt 1C :\n\nClasse énergie : D (198 kWh/m²/an)\nClasse climat : D (34 kg CO2/m²/an)\n\nLe logement est conforme aux obligations de location.\n\nRapport complet en pièce jointe.\n\nCordialement,\nDPE Express\n\n---\n📎 Pièce jointe : DPE_5acacias_1C.pdf (1.2 Mo)",
    },
]

# ---------------------------------------------------------------------------
# RECENT INBOX — Top 10 items in inbox (most recent, no relaylegacy response)
#
# Structure: 6 threads (2-4 msgs) + 4 standalone messages = 10 items
#
# TICKET 1 — Serrure cassée 15 rue des Lilas Apt 2A
#   Thread A (3 msgs): locataire signale → Thomas forward interne → locataire relance
#   Thread B (2 msgs): échange avec serrurier (devis + confirmation rdv)
#   Solo: facture du serrurier pour une intervention précédente sur même lot
#
# TICKET 2 — Fuite plafond SDB Rés. Les Tilleuls Apt 3A
#   Thread (2 msgs): locataire signale avec photo → plombier confirme RDV
#   Solo: message interne Thomas signalant dégât des eaux même appart
#
# + 3 threads indépendants + 2 solos indépendants
# ---------------------------------------------------------------------------

# === TICKET 1 — Thread A : Locataire signale serrure cassée (3 msgs) ===
FR_STORYLINES.append({
    "id": "recent_serrure_khelif_locataire",
    "thread_subject": "Serrure porte entrée cassée - 15 rue des Lilas Apt 2A",
    "emails": [
        {
            "archived": False,
            "from_name": "Sonia Khelif",
            "from_email": "s.khelif.loc@gmail.com",
            "subject": "Serrure porte entrée cassée - 15 rue des Lilas Apt 2A",
            "body": "Bonjour,\n\nMa serrure de porte d'entrée est cassée depuis hier soir, la clé tourne dans le vide et je n'arrive plus à fermer à clé. J'ai peur de laisser l'appart ouvert la nuit.\n\nPouvez-vous envoyer un serrurier en urgence svp ?\n\nMerci,\nSonia Khelif\nApt 2A, 15 rue des Lilas\n\n---\n📎 Pièce jointe : photo_serrure_cassee.jpg (1.2 Mo)",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Serrure porte entrée cassée - 15 rue des Lilas Apt 2A",
            "body": "Alexandre,\n\nJe forward le mail de Mme Khelif. J'ai appelé Serrurerie Rapide, ils envoient quelqu'un cet aprem normalement. Tu peux prévenir la locataire ?\n\nThomas",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Sonia Khelif",
            "from_email": "s.khelif.loc@gmail.com",
            "subject": "Re: Serrure porte entrée cassée - 15 rue des Lilas Apt 2A",
            "body": "Bonjour,\n\nJe n'ai toujours pas de nouvelles du serrurier. Il est 16h et personne n'est passé. Je ne peux pas fermer ma porte.\n\nMerci de me rappeler svp.\n\nS. Khelif",
            "is_reply": True,
        },
    ],
})

# === TICKET 1 — Thread B : Serrurier répond (thread séparé, 2 msgs) ===
FR_STORYLINES.append({
    "id": "recent_serrure_khelif_serrurier",
    "thread_subject": "Intervention serrure 15 rue des Lilas Apt 2A",
    "emails": [
        {
            "archived": False,
            "from_name": "Serrurerie Rapide 93",
            "from_email": "contact@serrurerie-rapide93.fr",
            "subject": "Intervention serrure 15 rue des Lilas Apt 2A",
            "body": "Bonjour M. Morel,\n\nSuite à votre appel, je peux passer cet après-midi entre 14h et 15h pour le changement de cylindre au 15 rue des Lilas, Apt 2A.\n\nSi c'est un cylindre européen standard, comptez environ 120€ TTC (fourniture + pose). Si le barillet est blindé, ça peut monter à 180€.\n\nMerci de confirmer.\n\nCordialement,\nM. Benali\nSerrurerie Rapide 93",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Serrurerie Rapide 93",
            "from_email": "contact@serrurerie-rapide93.fr",
            "subject": "Re: Intervention serrure 15 rue des Lilas Apt 2A",
            "body": "M. Morel,\n\nDésolé pour le retard, on a eu une urgence avant. Je serai sur place à 16h30 maximum.\n\nLa locataire est chez elle ?\n\nBenali",
            "is_reply": True,
        },
    ],
})

# === TICKET 2 — Thread : Fuite plafond Diallo (2 msgs : locataire + plombier) ===
FR_STORYLINES.append({
    "id": "recent_fuite_plafond_diallo",
    "thread_subject": "Fuite plafond salle de bain - Rés. Les Tilleuls Apt 3A",
    "emails": [
        {
            "archived": False,
            "from_name": "Amina Diallo",
            "from_email": "a.diallo.loc@gmail.com",
            "subject": "Fuite plafond salle de bain - Rés. Les Tilleuls Apt 3A",
            "body": "bonjour\n\nj'ai une grosse tache d'eau au plafond de la salle de bain, ça grossit depuis hier et maintenant ça goutte. je pense que ça vient de l'appart du dessus.\n\nc'est urgent svp\n\namina diallo\napt 3A rés les tilleuls\n\n---\n📎 Pièce jointe : photo_plafond_sdb_1.jpg (1.4 Mo)\n📎 Pièce jointe : photo_plafond_sdb_2.jpg (980 Ko)",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Duplex Plomberie",
            "from_email": "contact@duplex-plomberie.fr",
            "subject": "Re: Fuite plafond salle de bain - Rés. Les Tilleuls Apt 3A",
            "body": "Bonjour M. Morel,\n\nSuite à votre demande pour la recherche de fuite à la Résidence Les Tilleuls (infiltration depuis le 4A vers le 3A), nous pouvons intervenir demain matin à 9h.\n\nIl faudra accéder aux deux appartements (3A et 4A). Merci de prévenir les locataires.\n\nDevis estimatif en PJ.\n\nCordialement,\nDuplex Plomberie\n\n---\n📎 Pièce jointe : devis_recherche_fuite_tilleuls.pdf (67 Ko)",
            "is_reply": True,
        },
    ],
})

# === Thread indépendant 1 : EDL sortie Rodriguez avec multi-PJ (3 msgs) ===
FR_STORYLINES.append({
    "id": "recent_edl_rodriguez",
    "thread_subject": "EDL sortie Rodriguez - 5 impasse des Acacias Apt 1C",
    "emails": [
        {
            "archived": False,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "EDL sortie Rodriguez - 5 impasse des Acacias Apt 1C",
            "body": "Bonjour,\n\nJ'ai fait l'état des lieux de sortie ce matin. Quelques dégradations à noter :\n\n- Plan de travail cuisine : brûlure de cigarette\n- Mur salon : trous non rebouchés x4\n- Moquette chambre : tache importante\n- Salle de bain : joint silicone noirci\n\nPhotos, grille EDL et comparatif entrée/sortie en PJ.\n\nThomas\n\n---\n📎 Pièce jointe : EDL_sortie_Rodriguez_5acacias_1C.pdf (2.1 Mo)\n📎 Pièce jointe : photos_EDL_cuisine_salon.jpg (4.8 Mo)\n📎 Pièce jointe : comparatif_EDL_entree_sortie.xlsx (45 Ko)",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Sophie Marchand",
            "from_email": "s.marchand@elron-gestion.fr",
            "subject": "Re: EDL sortie Rodriguez - 5 impasse des Acacias Apt 1C",
            "body": "Thomas,\n\nPour la brûlure plan de travail, Rodriguez conteste (il dit que c'était là à l'entrée). La photo d'entrée est floue sur cette zone. Ton avis ?\n\nSophie",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: EDL sortie Rodriguez - 5 impasse des Acacias Apt 1C",
            "body": "Sophie,\n\nHonnêtement dans le doute je proposerai de réduire la retenue à 75€ au lieu de 150€. Ça évitera un conflit.\n\nDans tous les cas le remboursement de caution ne doit pas dépasser 375€ vu les autres dégradations.\n\nThomas",
            "is_reply": True,
        },
    ],
})

# === Thread indépendant 2 : Volet roulant Vasseur (2 msgs) ===
FR_STORYLINES.append({
    "id": "recent_volet_vasseur",
    "thread_subject": "Volet roulant bloqué chambre - 5 impasse Acacias Apt 2A",
    "emails": [
        {
            "archived": False,
            "from_name": "Claire Vasseur",
            "from_email": "c.vasseur.loc@gmail.com",
            "subject": "Volet roulant bloqué chambre - 5 impasse Acacias Apt 2A",
            "body": "Bonjour,\n\nLe volet roulant de la chambre est complètement bloqué en position fermée depuis ce matin. La sangle ne remonte plus du tout, on est dans le noir.\n\nC'est la 2ème fois en 3 mois. Ma fille dort dans cette chambre.\n\nMerci d'envoyer quelqu'un rapidement.\n\nClaire Vasseur\nApt 2A",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Menuiserie Caron",
            "from_email": "atelier@menuiserie-caron.fr",
            "subject": "Re: Volet roulant bloqué chambre - 5 impasse Acacias Apt 2A",
            "body": "Bonjour M. Lefèvre,\n\nC'est le 2ème blocage en peu de temps, le mécanisme d'enroulement est probablement HS. Il faudra remplacer l'ensemble (sangle + enrouleur + treuil).\n\nDevis en PJ. Je peux passer après-demain matin si vous validez.\n\nCordialement,\nMenuiserie Caron\n\n---\n📎 Pièce jointe : devis_volet_acacias_2A.pdf (56 Ko)",
            "is_reply": True,
        },
    ],
})

# === Thread indépendant 3 : Chauffage panne récente (4 msgs) ===
FR_STORYLINES.append({
    "id": "recent_chauffage_dupont",
    "thread_subject": "Plus de chauffage depuis ce matin - 8 av Foch",
    "emails": [
        {
            "archived": False,
            "from_name": "Marc Dupont",
            "from_email": "m.dupont.locataire@gmail.com",
            "subject": "Plus de chauffage depuis ce matin - 8 av Foch",
            "body": "Bonjour,\n\nPLUS DE CHAUFFAGE depuis ce matin dans tout l'immeuble au 8 avenue Foch. Il fait 14 degrés chez moi. Ma femme est enceinte de 7 mois.\n\nC'est la 3ème fois cet hiver !!\n\nM. Dupont\nApt 2B",
            "is_reply": False,
        },
        {
            "archived": False,
            "from_name": "Isabelle Martin",
            "from_email": "i.martin.loc@gmail.com",
            "subject": "Re: Plus de chauffage depuis ce matin - 8 av Foch",
            "body": "Pareil chez moi au 2A, les radiateurs sont froids. C'est quand même incroyable en plein hiver.\n\nI. Martin",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "Thomas Lefèvre",
            "from_email": "t.lefevre@elron-gestion.fr",
            "subject": "Re: Plus de chauffage depuis ce matin - 8 av Foch",
            "body": "Bonjour M. Dupont, Mme Martin,\n\nJ'ai contacté ThermoConfort, un technicien sera sur place d'ici 2h maximum. Je vous tiens au courant.\n\nCordialement,\nThomas Lefèvre",
            "is_reply": True,
        },
        {
            "archived": False,
            "from_name": "ThermoConfort SARL",
            "from_email": "devis@thermoconfort.fr",
            "subject": "Re: Plus de chauffage depuis ce matin - 8 av Foch",
            "body": "M. Lefèvre,\n\nOn est sur place. C'est le brûleur qui a lâché cette fois. Réparation en cours, chauffage devrait être rétabli d'ici 1h.\n\nPar contre, cette chaudière a 18 ans et les pannes vont se multiplier. Je vous recommande sérieusement de planifier un remplacement.\n\nCordialement,\nThermoConfort",
            "is_reply": True,
        },
    ],
})

# ---------------------------------------------------------------------------
# RECENT INBOX SOLO — 4 emails solo "reçus aujourd'hui" sans réponse user
# ---------------------------------------------------------------------------
FR_RECENT_INBOX_SOLO = [
    # TICKET 1 — Solo : Facture serrurier pour intervention précédente même lot
    {
        "from_name": "Serrurerie Rapide 93",
        "from_email": "contact@serrurerie-rapide93.fr",
        "subject": "Facture intervention serrure 15 rue des Lilas - FAC-2026-SR018",
        "body": "Bonjour M. Morel,\n\nVeuillez trouver ci-joint la facture pour l'intervention de ce jour au 15 rue des Lilas, Apt 2A (remplacement cylindre européen).\n\nMontant TTC : 132€\n\nMerci de procéder au règlement sous 30 jours.\n\nCordialement,\nSerrurerie Rapide 93\n\n---\n📎 Pièce jointe : facture_SR-2026-0018.pdf (43 Ko)",
    },
    # TICKET 2 — Solo : Message interne Thomas signalant dégât même appart Tilleuls
    {
        "from_name": "Thomas Lefèvre",
        "from_email": "t.lefevre@elron-gestion.fr",
        "subject": "Dégât des eaux confirmé Tilleuls 3A - à déclarer assurance",
        "body": "Alexandre,\n\nJe suis passé voir Mme Diallo (Apt 3A Tilleuls). C'est bien une fuite venant du 4A au-dessus. Le plafond de la SDB est bien abîmé, il faudra refaire.\n\nOn doit déclarer à l'assurance rapidement. Tu peux t'en occuper ?\n\nThomas",
    },
    # Solo indépendant 1 : Rappel réunion (info interne)
    {
        "from_name": "Sophie Marchand",
        "from_email": "s.marchand@elron-gestion.fr",
        "subject": "Rappel : réunion équipe lundi 9h",
        "body": "Bonjour à tous,\n\nJuste un rappel pour la réunion de lundi matin. On se retrouve au bureau à 9h. Ordre du jour envoyé vendredi.\n\nBon week-end,\nSophie",
    },
    # Solo indépendant 2 : Locataire remercie (pas de réponse nécessaire)
    {
        "from_name": "Patrick Leroy",
        "from_email": "p.leroy.locataire@gmail.com",
        "subject": "Merci pour l'ascenseur",
        "body": "Bonjour M. Morel,\n\nJe voulais juste vous dire merci, l'ascenseur a été réparé ce matin et il marche parfaitement. Quel soulagement après 2 semaines !\n\nBonne journée,\nP. Leroy\n15 rue des Lilas",
    },
]

# ---------------------------------------------------------------------------
# Filler templates for FR emails
# ---------------------------------------------------------------------------
_FR_FILLER_TENANTS = [
    ("Paul Girard", "p.girard.loc@gmail.com", "Rés. Les Tilleuls, Montreuil", "4B"),
    ("Sonia Khelif", "s.khelif.loc@gmail.com", "15 rue des Lilas, Paris", "2A"),
    ("Michel Bonnet", "m.bonnet.loc@gmail.com", "42 bd Gambetta, Bordeaux", "1C"),
    ("Lucie Perrot", "l.perrot.tenant@gmail.com", "8 avenue Foch, Boulogne", "3A"),
    ("David Chen", "d.chen.loc@gmail.com", "23 rue Voltaire, Lyon", "3B"),
    ("Martine Jolivet", "m.jolivet.loc@gmail.com", "17 rue du Marché, Nantes", "1B"),
    ("Rachid Mansouri", "r.mansouri.loc@gmail.com", "Rés. Le Clos Fleuri, Bordeaux", "3C"),
    ("Claire Vasseur", "c.vasseur.loc@gmail.com", "5 impasse des Acacias, Toulouse", "2A"),
    ("Bruno Picard", "b.picard.tenant@gmail.com", "Rés. Les Tilleuls, Montreuil", "2B"),
    ("Samira Lahlou", "s.lahlou.loc@gmail.com", "15 rue des Lilas, Paris", "5A"),
]

_FR_RENT_SUBJECTS = [
    "Virement loyer {month} effectué",
    "Loyer {month} - virement fait",
    "Confirmation paiement loyer {month}",
    "Loyer {month} payé",
    "Re: Appel de loyer {month}",
]

_FR_RENT_BODIES = [
    "Bonjour,\n\nJe vous confirme le virement du loyer de {month}.\n\nCordialement,\n{name}",
    "Bonjour, virement du loyer de {month} effectué ce jour.\n\n{name}",
    "Bonjour,\n\nLoyer de {month} viré comme d'habitude.\n\nCdt,\n{name}\n{addr}",
    "Le virement pour {month} a été fait. Merci.\n\n{name}",
    "Bonjour,\n\nPaiement loyer {month} OK. Pourriez-vous m'envoyer la quittance svp ?\n\nMerci,\n{name}",
]

_FR_MAINT_SUBJECTS = [
    "Problème {issue} - {addr}",
    "{issue} à signaler - {addr}",
    "Signalement {issue}",
    "Signalement : {issue} - {addr}",
]

_FR_MAINT_ISSUES = [
    "robinet qui fuit", "prise électrique HS", "porte qui ferme mal",
    "fenêtre qui ne ferme plus", "WC bouché", "tache au plafond",
    "VMC bruyante", "store cassé", "sonnette HS", "peinture qui s'écaille",
    "évier bouché", "radiateur qui ne chauffe pas", "joint de douche moisi",
]

_FR_MAINT_BODIES = [
    "Bonjour,\n\nJe vous signale un problème de {issue} dans mon appartement ({addr}). Pourriez-vous envoyer quelqu'un ?\n\nMerci,\n{name}",
    "Bonjour,\n\nJ'ai un souci de {issue}. C'est pas très grave mais ça m'embête au quotidien. Quand est-ce que quelqu'un peut passer ?\n\nCordialement,\n{name}\n{addr}",
    "bonjour\n\nproblème de {issue} chez moi. merci de faire le nécessaire.\n\n{name}",
    "Bonjour,\n\nCa fait un moment que j'ai un problème de {issue} mais je n'osais pas vous déranger. Là ça commence à être vraiment gênant. Est-ce possible d'envoyer un artisan ?\n\nMerci d'avance,\n{name}\nApt {unit}, {addr}",
]

_FR_QUESTION_SUBJECTS = [
    "Question sur le bail",
    "Renseignement charges",
    "Question assurance habitation",
    "Demande d'information",
    "Question travaux",
]

_FR_QUESTION_BODIES = [
    "Bonjour,\n\nJ'aurais une question concernant mon bail. Est-ce que je peux sous-louer une chambre pendant mon absence en août ?\n\nMerci,\n{name}",
    "Bonjour,\n\nPourriez-vous me détailler les charges locatives svp ? Je trouve le montant élevé ce mois-ci.\n\nCordialement,\n{name}\n{addr}",
    "Bonjour,\n\nMon assurance habitation me demande une attestation du propriétaire. Pouvez-vous m'en fournir une ?\n\nMerci,\n{name}",
    "Bonjour,\n\nEst-ce que j'ai le droit de repeindre les murs de mon appartement ? Je voudrais changer la couleur du salon.\n\nMerci,\n{name}\n{addr}",
    "Bonjour,\n\nJe voulais savoir si le local vélo dans le sous-sol est accessible à tous les locataires ou s'il faut réserver une place ?\n\n{name}",
]

_FR_MONTHS = [
    "octobre", "novembre", "décembre", "janvier",
    "septembre", "août", "juillet",
]

_FR_INTERNAL_SUBJECTS = [
    "Point rapide {topic}",
    "Info : {topic}",
    "Re: {topic}",
    "A voir : {topic}",
]

_FR_INTERNAL_TOPICS = [
    "visite des Tilleuls", "planning congés février", "stock de produits ménagers",
    "réunion syndic jeudi", "formation logiciel", "appel proprio Blanchard",
    "dossier CAF Diallo", "relance assurance", "problème courrier Gambetta",
]

_FR_INTERNAL_BODIES = [
    "{topic} → on en parle demain ?\n\n{name}",
    "Salut,\n\nPetit point sur {topic}. Tu es dispo cet aprèm pour en discuter 5 min ?\n\n{name}",
    "Bonjour,\n\nJuste pour info : {topic}, c'est réglé.\n\nBonne journée,\n{name}",
    "Hello,\n\nTu as avancé sur {topic} ? Le proprio me relance.\n\nMerci,\n{name}",
]


def _generate_fr_filler(count: int, section: str) -> list:
    """Generate French filler emails."""
    rng = _random.Random(f"elron-fr-filler-{section}")
    filler = []
    is_archived = section == "archived"

    for i in range(count):
        roll = rng.random()

        if roll < 0.35:
            # Rent confirmation
            tenant = rng.choice(_FR_FILLER_TENANTS)
            name, email, addr, unit = tenant
            month = rng.choice(_FR_MONTHS)
            subj = rng.choice(_FR_RENT_SUBJECTS).format(month=month, name=name)
            body = rng.choice(_FR_RENT_BODIES).format(month=month, name=name, addr=addr, unit=unit)
            filler.append({
                "from_name": name, "from_email": email,
                "subject": subj, "body": body,
                "archived": is_archived,
            })

        elif roll < 0.60:
            # Maintenance request
            tenant = rng.choice(_FR_FILLER_TENANTS)
            name, email, addr, unit = tenant
            issue = rng.choice(_FR_MAINT_ISSUES)
            subj = rng.choice(_FR_MAINT_SUBJECTS).format(issue=issue, addr=addr)
            body = rng.choice(_FR_MAINT_BODIES).format(issue=issue, name=name, addr=addr, unit=unit)
            filler.append({
                "from_name": name, "from_email": email,
                "subject": subj, "body": body,
                "archived": is_archived,
            })

        elif roll < 0.75:
            # Question
            tenant = rng.choice(_FR_FILLER_TENANTS)
            name, email, addr, unit = tenant
            subj = rng.choice(_FR_QUESTION_SUBJECTS)
            body = rng.choice(_FR_QUESTION_BODIES).format(name=name, addr=addr, unit=unit)
            filler.append({
                "from_name": name, "from_email": email,
                "subject": subj, "body": body,
                "archived": is_archived,
            })

        else:
            # Internal message
            person = rng.choice(FR_INTERNAL)
            name, email, _ = person
            topic = rng.choice(_FR_INTERNAL_TOPICS)
            subj = rng.choice(_FR_INTERNAL_SUBJECTS).format(topic=topic)
            body = rng.choice(_FR_INTERNAL_BODIES).format(topic=topic, name=name)
            filler.append({
                "from_name": name, "from_email": email,
                "subject": subj, "body": body,
                "archived": is_archived,
            })

    return filler


# ---------------------------------------------------------------------------
# Main function: return all ~300 emails ordered (archived first, inbox last)
# ---------------------------------------------------------------------------
def get_fr_full_emails() -> list:
    """Return ~300 French emails: first 270 archived, last 30 inbox.

    Inbox is split into two ordered blocks:
      - Positions 0-19: "older" inbox with user replies (threads where relaylegacy responded)
      - Positions 20-29: "today" inbox — 4 solo + 6 threads, no relaylegacy response, some with PJ
    This ordering means the last 10 items (most recent dates) are "today's" emails.
    """
    archived = []
    inbox_older = []   # Inbox emails with user (relaylegacy) responses
    inbox_recent = []  # Inbox emails received "today" — no user response

    # Collect storyline emails
    for storyline in FR_STORYLINES:
        is_recent = storyline["id"].startswith("recent_")
        for email in storyline["emails"]:
            entry = {
                **email,
                "storyline_id": storyline["id"],
                "thread_subject": storyline["thread_subject"],
                "is_reply": email.get("is_reply", False),
            }
            if email.get("archived", True):
                archived.append(entry)
            elif is_recent:
                inbox_recent.append(entry)
            else:
                inbox_older.append(entry)

    # Collect standalone archived
    for email in FR_STANDALONE_ARCHIVED:
        archived.append({
            **email,
            "archived": True,
            "storyline_id": None,
            "thread_subject": None,
            "is_reply": False,
        })

    # Collect standalone inbox (older — with user replies)
    for email in FR_STANDALONE_INBOX:
        inbox_older.append({
            **email,
            "archived": False,
            "storyline_id": None,
            "thread_subject": None,
            "is_reply": False,
        })

    # Collect recent solo inbox emails
    for email in FR_RECENT_INBOX_SOLO:
        inbox_recent.append({
            **email,
            "archived": False,
            "storyline_id": None,
            "thread_subject": None,
            "is_reply": False,
        })

    # Pad archived with filler to reach target
    archived_target = 270
    inbox_target = 30

    if len(archived) < archived_target:
        filler = _generate_fr_filler(archived_target - len(archived), "archived")
        for f in filler:
            archived.append({
                **f,
                "storyline_id": None,
                "thread_subject": None,
                "is_reply": False,
            })

    # Build final inbox: older first, then recent (top 10 items)
    # inbox_recent contains the 10 most recent items (6 threads + 4 solos)
    # inbox_older fills the rest up to inbox_target
    older_count = inbox_target - len(inbox_recent)
    inbox = inbox_older[:max(older_count, 0)] + inbox_recent

    # If we still need more inbox, pad with filler
    if len(inbox) < inbox_target:
        filler = _generate_fr_filler(inbox_target - len(inbox), "inbox")
        for f in filler:
            inbox.append({
                **f,
                "storyline_id": None,
                "thread_subject": None,
                "is_reply": False,
            })

    # Return archived (first 270) then inbox (last 30)
    return archived[:archived_target] + inbox[:inbox_target]
