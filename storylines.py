"""
Pre-authored, interconnected email storylines for the Elron Inbox Simulator.
Batches: history, day1, day2, day3, day4, month1, month2
"""

# ---------------------------------------------------------------------------
# Expanded contractor roster
# ---------------------------------------------------------------------------
CONTRACTORS = [
    ("Summit Elevator Services", "summit.elevator.svc@gmail.com"),
    ("Bob's Plumbing", "bob.plumbing.co@gmail.com"),
    ("Ace HVAC Services", "ace.hvac.quotes@gmail.com"),
    ("City Electric Co.", "cityelectric.bids@gmail.com"),
    ("ProFix Contractors", "profix.contractors@gmail.com"),
    ("QuickRepair LLC", "quickrepair.quotes@gmail.com"),
    ("Metro Roofing Inc.", "metro.roofing.bids@gmail.com"),
    ("AllPro Maintenance", "allpro.maintenance@gmail.com"),
    ("Sunrise Pest Control", "sunrise.pest.quotes@gmail.com"),
    ("Premier Appliance Repair", "premier.appliance.svc@gmail.com"),
    ("GreenLeaf Landscaping", "greenleaf.quotes@gmail.com"),
    ("FastFix General Contractors", "fastfix.gc.quotes@gmail.com"),
    ("BlueSky Windows & Doors", "bluesky.wd.bids@gmail.com"),
    ("SafeGuard Locksmith", "safeguard.locksmith@gmail.com"),
    ("ClearView Glass & Mirror", "clearview.glass@gmail.com"),
    ("TruSeal Waterproofing", "truseal.waterproof@gmail.com"),
    ("BrightStar Cleaning Co.", "brightstar.cleaning@gmail.com"),
    ("Redline Fire Safety", "redline.firesafety@gmail.com"),
    ("EcoMold Remediation", "ecomold.remediation@gmail.com"),
    ("Atlas Drywall & Paint", "atlas.drywall@gmail.com"),
]

# ---------------------------------------------------------------------------
# STORYLINES - each is a dict with id, thread_subject, emails[]
# ---------------------------------------------------------------------------
STORYLINES = []

# === 1. ELEVATOR v1 — past incident (history) ===
STORYLINES.append({
    "id": "elevator_v1",
    "thread_subject": "Elevator issue - 92 Hawthorn Gardens",
    "emails": [
        {
            "batch": "history",
            "from_name": "Sean Murphy",
            "from_email": "sean.murphy.renter@gmail.com",
            "subject": "Elevator issue - 92 Hawthorn Gardens",
            "body": "Hi,\n\nJust wanted to let you know the elevator at 92 Hawthorn Gardens has been making a grinding noise for the past couple of days. It still works but it sounds concerning. Could you have someone look at it?\n\nThanks,\nSean Murphy\nUnit 101",
            "is_reply": False,
        },
        {
            "batch": "history",
            "from_name": "Summit Elevator Services",
            "from_email": "summit.elevator.svc@gmail.com",
            "subject": "Re: Elevator issue - 92 Hawthorn Gardens",
            "body": "Hi,\n\nWe inspected the elevator at 92 Hawthorn Gardens today. The issue was a worn guide shoe on the 3rd floor landing. We've replaced it and lubricated the rails. Everything is running smoothly now.\n\nInvoice #SE-4821 for $485.00 is attached.\n\nLabour (2 hrs @ $125/hr): $250.00\nParts (guide shoe assembly): $185.00\nService call fee: $50.00\nTotal: $485.00\n\nPayment due within 30 days.\n\nBest regards,\nMike Torres\nSummit Elevator Services",
            "is_reply": True,
        },
        {
            "batch": "history",
            "from_name": "Derek Cooper",
            "from_email": "derek.cooper.apt@gmail.com",
            "subject": "Re: Elevator issue - 92 Hawthorn Gardens",
            "body": "Took you long enough. The elevator was making that noise for DAYS before anyone bothered to do anything about it. I pay good money to live here and I expect things to be maintained properly. This building is going downhill.\n\nDerek Cooper\nUnit 301",
            "is_reply": True,
        },
    ],
})

# === 2. ELEVATOR v2 — breaks again (day1-day4) ===
# Each tenant emails INDEPENDENTLY about the same issue (no cross-tenant threading).
# The AI should recognize these are about the same problem and group them.
STORYLINES.append({
    "id": "elevator_v2_sean",
    "thread_subject": "Elevator broken AGAIN - 92 Hawthorn Gardens",
    "emails": [
        {
            "batch": "day1",
            "from_name": "Sean Murphy",
            "from_email": "sean.murphy.renter@gmail.com",
            "subject": "Elevator broken AGAIN - 92 Hawthorn Gardens",
            "body": "Hi,\n\nI'm sorry to report that the elevator at 92 Hawthorn Gardens is out of service again as of this morning. The doors open but the cab won't move. I tried pressing all the buttons but nothing happens.\n\nI know it was just fixed a few weeks ago so this is frustrating. Could you contact the elevator company again?\n\nThanks,\nSean Murphy\nUnit 101",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "elevator_v2_vanessa",
    "thread_subject": "Elevator not working - 92 Hawthorn Gardens",
    "emails": [
        {
            "batch": "day1",
            "from_name": "Vanessa Rivera",
            "from_email": "v.rivera.tenant@gmail.com",
            "subject": "Elevator not working - 92 Hawthorn Gardens",
            "body": "Hi,\n\nI'm writing to let you know the elevator is not working. I tried it around 8 AM and it's completely dead. I'm on the 2nd floor so stairs are manageable for me, but I'm worried about Mrs. Richardson on the 4th floor \u2014 she has mobility issues.\n\nPlease let us know when it will be fixed.\n\nThank you,\nVanessa Rivera\nUnit 201",
            "is_reply": False,
        },
        {
            "batch": "day4",
            "from_name": "Vanessa Rivera",
            "from_email": "v.rivera.tenant@gmail.com",
            "subject": "Re: Elevator not working - 92 Hawthorn Gardens",
            "body": "Hi,\n\nJust wanted to say thank you for getting the elevator fixed. It's running great now. I know these things take time and I appreciate you handling it.\n\nBest,\nVanessa\nUnit 201",
            "is_reply": True,
        },
    ],
})

STORYLINES.append({
    "id": "elevator_v2_derek",
    "thread_subject": "ELEVATOR BROKEN - 92 Hawthorn Gardens - UNACCEPTABLE",
    "emails": [
        {
            "batch": "day1",
            "from_name": "Derek Cooper",
            "from_email": "derek.cooper.apt@gmail.com",
            "subject": "ELEVATOR BROKEN - 92 Hawthorn Gardens - UNACCEPTABLE",
            "body": "Are you KIDDING me?? The elevator is broken AGAIN?? I literally just complained about the state of this building and now this happens. I'm on the 3rd floor and I have a bad knee. This is completely unacceptable.\n\nI want to know EXACTLY what's being done about this and when it will be fixed. If this isn't resolved by end of day I'm calling the housing authority. I'm also seriously considering withholding next month's rent until this building is properly maintained.\n\nThis is a joke.\n\nDerek Cooper\nUnit 301",
            "is_reply": False,
        },
        {
            "batch": "day2",
            "from_name": "Derek Cooper",
            "from_email": "derek.cooper.apt@gmail.com",
            "subject": "Re: ELEVATOR BROKEN - 92 Hawthorn Gardens - UNACCEPTABLE",
            "body": "TOMORROW?? Are you serious right now? The elevator has been broken since yesterday morning and the earliest anyone can come is TOMORROW?\n\nI had to carry my groceries up 3 flights of stairs. My knee is killing me. Meanwhile I'm paying $2,400 a month for an apartment with a broken elevator. What exactly am I paying for?\n\nThis is the second time in a month. Maybe it's time to find a competent elevator company. Or maybe I need to find a competent property manager.\n\nI expect a rent reduction for this inconvenience.\n\nDerek Cooper\nUnit 301",
            "is_reply": True,
        },
        {
            "batch": "day3",
            "from_name": "Derek Cooper",
            "from_email": "derek.cooper.apt@gmail.com",
            "subject": "Re: ELEVATOR BROKEN - 92 Hawthorn Gardens - UNACCEPTABLE",
            "body": "So it took 3 days to fix an elevator. Three days. And apparently the problem was something that should have been caught during the LAST repair. Great job everyone.\n\nI still expect a rent adjustment for the inconvenience. My knee is still swollen from hauling myself up and down the stairs.\n\nDerek Cooper\nUnit 301",
            "is_reply": True,
        },
        {
            "batch": "day4",
            "from_name": "Derek Cooper",
            "from_email": "derek.cooper.apt@gmail.com",
            "subject": "Re: ELEVATOR BROKEN - 92 Hawthorn Gardens - UNACCEPTABLE",
            "body": "Finally. Only took half the week.\n\nI'm still waiting to hear about the rent adjustment.\n\nDerek Cooper\nUnit 301",
            "is_reply": True,
        },
    ],
})

STORYLINES.append({
    "id": "elevator_v2_monica",
    "thread_subject": "Elevator out of order - 92 Hawthorn Gardens",
    "emails": [
        {
            "batch": "day1",
            "from_name": "Monica Richardson",
            "from_email": "m.richardson.lease@gmail.com",
            "subject": "Elevator out of order - 92 Hawthorn Gardens",
            "body": "Dear Property Manager,\n\nI hope this message finds you well. I'm writing because the elevator appears to be out of order again. As you may know, I'm 72 years old and live on the 4th floor. Climbing the stairs is very difficult for me, especially with groceries.\n\nMy daughter helped me get upstairs today but she can't be here every day. Could you please prioritize getting this fixed? I would be very grateful.\n\nThank you so much,\nMonica Richardson\nUnit 401",
            "is_reply": False,
        },
    ],
})

# Contractor thread for the elevator repair (only threads with PM, not tenants)
STORYLINES.append({
    "id": "elevator_v2_contractor",
    "thread_subject": "Elevator repair request - 92 Hawthorn Gardens",
    "emails": [
        {
            "batch": "day2",
            "from_name": "Summit Elevator Services",
            "from_email": "summit.elevator.svc@gmail.com",
            "subject": "Elevator repair request - 92 Hawthorn Gardens",
            "body": "Hi,\n\nThank you for contacting us about the elevator at 92 Hawthorn Gardens. We're sorry to hear it's having issues again.\n\nOur earliest available technician can be on-site tomorrow morning between 8-10 AM. Based on your description (doors open, cab won't move), it sounds like it could be a motor relay or control board issue \u2014 different from the guide shoe we replaced last time.\n\nWe'll diagnose the problem and provide a quote before proceeding with any repairs.\n\nBest regards,\nMike Torres\nSummit Elevator Services\n(555) 234-8901",
            "is_reply": False,
        },
        {
            "batch": "day3",
            "from_name": "Summit Elevator Services",
            "from_email": "summit.elevator.svc@gmail.com",
            "subject": "Re: Elevator repair request - 92 Hawthorn Gardens",
            "body": "Hi,\n\nOur technician completed the repair at 92 Hawthorn Gardens this morning. Here's the summary:\n\nDIAGNOSIS: The main drive motor contactor was failing intermittently, causing the cab to lose power after the doors opened. Additionally, we found a worn cable sheave bearing that was contributing to the grinding noise reported previously.\n\nWORK PERFORMED:\n- Replaced main motor contactor\n- Replaced cable sheave bearing\n- Tested all safety interlocks\n- Lubricated all moving components\n- Full operational test (50 cycles, all floors)\n\nInvoice #SE-4867\nLabour (4.5 hrs @ $125/hr): $562.50\nParts (motor contactor): $340.00\nParts (sheave bearing): $215.00\nService call fee: $50.00\nTotal: $1,167.50\n\nThe elevator is now fully operational. We recommend a full annual inspection within the next 3 months given the age of this unit.\n\nPayment due within 30 days.\n\nBest regards,\nMike Torres\nSummit Elevator Services",
            "is_reply": True,
        },
    ],
})

# === 3. BURST PIPE — 45 Maple Avenue (SHOWCASE) ===
STORYLINES.append({
    "id": "burst_pipe",
    "thread_subject": "URGENT - Burst pipe in Unit 3C - 45 Maple Avenue",
    "emails": [
        {
            "batch": "day1",
            "from_name": "Daniel White",
            "from_email": "d.white.apt12@gmail.com",
            "subject": "URGENT - Burst pipe in Unit 3C - 45 Maple Avenue",
            "body": "Hi,\n\nEMERGENCY \u2014 a pipe has burst under my kitchen sink in Unit 3C at 45 Maple Avenue. Water is spraying everywhere. I've turned off the valve under the sink but water is still pooling on the floor and I think it's going through to the unit below.\n\nI've put down every towel I own but this needs a plumber ASAP. Please call me at (555) 312-7744.\n\nDaniel White\nUnit 3C, 45 Maple Avenue",
            "is_reply": False,
        },
        {
            "batch": "day1",
            "from_name": "Patricia Jackson",
            "from_email": "p.jackson.tenant@gmail.com",
            "subject": "Water dripping from my ceiling - Unit 2B - 45 Maple Avenue",
            "body": "Hi,\n\nI just got home and there's water dripping from my kitchen ceiling in Unit 2B. It's coming through the light fixture which is really concerning \u2014 I've switched off the breaker for that circuit.\n\nThere's a growing stain on the ceiling and the dripping is getting worse. I think it might be coming from the unit above me (3C). Could you please send someone right away?\n\nThank you,\nPatricia Jackson\nUnit 2B, 45 Maple Avenue",
            "is_reply": False,
        },
        {
            "batch": "day2",
            "from_name": "Bob's Plumbing",
            "from_email": "bob.plumbing.co@gmail.com",
            "subject": "Re: URGENT - Burst pipe in Unit 3C - 45 Maple Avenue",
            "body": "Hi,\n\nWe received your emergency call and our technician Dave visited 45 Maple Avenue this afternoon. Here's what we found:\n\nThe cold water supply line under the kitchen sink in Unit 3C had a corroded fitting that gave way. We've done a temporary patch to stop the leak and turned the water back on. However, the fitting and a section of pipe need to be fully replaced.\n\nWe'll have a formal quote to you by tomorrow. The temporary fix will hold for now but I'd recommend scheduling the full repair within the week.\n\nRegarding Unit 2B below \u2014 the ceiling drywall will need to dry out before we can assess if it needs replacement. I'd give it 48-72 hours.\n\nBest,\nBob Henderson\nBob's Plumbing\n(555) 891-2345",
            "is_reply": True,
        },
        {
            "batch": "day3",
            "from_name": "Bob's Plumbing",
            "from_email": "bob.plumbing.co@gmail.com",
            "subject": "Re: URGENT - Burst pipe in Unit 3C - 45 Maple Avenue",
            "body": "Hi,\n\nAs promised, here's our quote for the full repair at Unit 3C, 45 Maple Avenue:\n\nSCOPE OF WORK:\n- Remove and replace corroded cold water supply line (approx 4 ft)\n- Replace shut-off valve\n- Replace supply line fitting and connector to sink\n- Pressure test all connections\n- Inspect adjacent pipes for similar corrosion\n\nQuote #BP-2024-0892\nLabour (3 hrs @ $95/hr): $285.00\nMaterials (copper pipe, fittings, valve): $165.00\nTotal: $450.00\n\nWe can schedule the work for any day this week. Please confirm and we'll get it done.\n\nBest,\nBob Henderson\nBob's Plumbing",
            "is_reply": True,
        },
        {
            "batch": "day4",
            "from_name": "Bob's Plumbing",
            "from_email": "bob.plumbing.co@gmail.com",
            "subject": "Invoice - Pipe repair Unit 3C, 45 Maple Avenue",
            "body": "Hi,\n\nThe pipe repair at Unit 3C, 45 Maple Avenue has been completed. All connections have been pressure tested and are holding perfectly.\n\nInvoice #BP-2024-0893\nEmergency call-out (Day 1): $150.00\nLabour (3.5 hrs @ $95/hr): $332.50\nMaterials: $165.00\nTotal: $647.50\n\nPayment due within 30 days.\n\nThanks for your business.\n\nBob Henderson\nBob's Plumbing",
            "is_reply": False,
        },
        {
            "batch": "day4",
            "from_name": "Patricia Jackson",
            "from_email": "p.jackson.tenant@gmail.com",
            "subject": "Re: Water dripping from my ceiling - Unit 2B - 45 Maple Avenue",
            "body": "Hi,\n\nThe dripping has stopped since the pipe was fixed upstairs, thank you. However there's a large brown stain on my kitchen ceiling and the drywall feels soft in one spot. Will someone be coming to repair the ceiling damage?\n\nAlso, the area around the light fixture still looks damp. I'm keeping the breaker off for safety but I'd like to be able to use my kitchen light again.\n\nThank you,\nPatricia Jackson\nUnit 2B",
            "is_reply": True,
        },
        {
            "batch": "month1",
            "from_name": "Daniel White",
            "from_email": "d.white.apt12@gmail.com",
            "subject": "Re: URGENT - Burst pipe in Unit 3C - 45 Maple Avenue",
            "body": "Hi,\n\nJust following up \u2014 the pipe repair is holding up great, no issues there. But the wall behind where the pipe burst has some water damage and the paint is peeling. Any timeline on when that will be patched up?\n\nThanks,\nDaniel White\nUnit 3C",
            "is_reply": True,
        },
        {
            "batch": "month1",
            "from_name": "Atlas Drywall & Paint",
            "from_email": "atlas.drywall@gmail.com",
            "subject": "Quote - Drywall repair, 45 Maple Avenue Units 2B & 3C",
            "body": "Hi,\n\nFollowing our site visit to 45 Maple Avenue, here's our quote for water damage repair:\n\nUnit 3C (kitchen wall):\n- Remove damaged drywall section (3 ft x 2 ft)\n- Install new drywall, tape, mud, and sand\n- Prime and paint to match\n\nUnit 2B (kitchen ceiling):\n- Remove water-damaged ceiling drywall (4 ft x 3 ft)\n- Replace light fixture housing (water damaged)\n- Install new drywall, tape, mud, and sand\n- Prime and paint to match\n\nQuote #AD-0334\nMaterials: $280.00\nLabour (8 hrs @ $75/hr): $600.00\nTotal: $880.00\n\nWe can start next Monday. Both units will need to be accessible.\n\nAtlas Drywall & Paint",
            "is_reply": False,
        },
    ],
})

# === 4. LATE RENT — Ryan Young (231 Elm Blvd, Unit 3) ===
STORYLINES.append({
    "id": "late_rent_ryan",
    "thread_subject": "Late rent payment - Unit 3, 231 Elm Blvd",
    "emails": [
        {
            "batch": "history",
            "from_name": "Ryan Young",
            "from_email": "ryan.young.tenant@gmail.com",
            "subject": "Late rent payment - Unit 3, 231 Elm Blvd",
            "body": "Hi,\n\nI wanted to give you a heads up that my rent for this month will be about a week late. I had some unexpected car repairs that wiped out my savings. I'll have the full amount to you by the 10th.\n\nSorry about this.\n\nRyan Young\nUnit 3, 231 Elm Blvd",
            "is_reply": False,
        },
        {
            "batch": "day1",
            "from_name": "Ryan Young",
            "from_email": "ryan.young.tenant@gmail.com",
            "subject": "Re: Late rent payment - Unit 3, 231 Elm Blvd",
            "body": "Hi,\n\nI'm really sorry but I need to let you know my rent is going to be late again this month. My hours at work got cut and I'm picking up extra shifts to make up the difference. I should be able to pay by the 12th.\n\nI know this is the second time and I apologize. I'm working on getting things stabilized.\n\nRyan Young\nUnit 3",
            "is_reply": True,
        },
        {
            "batch": "day3",
            "from_name": "Ryan Young",
            "from_email": "ryan.young.tenant@gmail.com",
            "subject": "Re: Late rent payment - Unit 3, 231 Elm Blvd",
            "body": "Hi,\n\nJust wanted to confirm I transferred the full rent amount this morning. It should show up in your account by tomorrow. Thanks for being patient with me.\n\nRyan\nUnit 3",
            "is_reply": True,
        },
    ],
})

# === 5. LEASE RENEWAL — Sarah Johnson (31 Harbor View Road) ===
STORYLINES.append({
    "id": "lease_renewal_sarah",
    "thread_subject": "Lease renewal - 31 Harbor View Road",
    "emails": [
        {
            "batch": "history",
            "from_name": "Sarah Johnson",
            "from_email": "sarah.j.tenant@gmail.com",
            "subject": "Lease renewal - 31 Harbor View Road",
            "body": "Hi,\n\nI received the lease renewal notice for 31 Harbor View Road. I'm definitely interested in staying \u2014 I love the house and the neighborhood. I just need a few days to review the new terms.\n\nThanks,\nSarah Johnson",
            "is_reply": False,
        },
        {
            "batch": "day2",
            "from_name": "Sarah Johnson",
            "from_email": "sarah.j.tenant@gmail.com",
            "subject": "Re: Lease renewal - 31 Harbor View Road",
            "body": "Hi,\n\nI've reviewed the renewal terms. I noticed the rent is going up by $150/month. Could you explain what's driving the increase? The property hasn't had any major upgrades since I moved in.\n\nAlso, is there any flexibility if I sign a 2-year lease instead of 1 year?\n\nThanks,\nSarah",
            "is_reply": True,
        },
        {
            "batch": "day3",
            "from_name": "Sarah Johnson",
            "from_email": "sarah.j.tenant@gmail.com",
            "subject": "Re: Lease renewal - 31 Harbor View Road",
            "body": "Hi,\n\nThank you for explaining. The market rate comparison makes sense. I'll go ahead and renew for 12 months at the new rate. Could you send over the paperwork?\n\nBest,\nSarah",
            "is_reply": True,
        },
        {
            "batch": "month1",
            "from_name": "Sarah Johnson",
            "from_email": "sarah.j.tenant@gmail.com",
            "subject": "Re: Lease renewal - 31 Harbor View Road",
            "body": "Hi,\n\nI've signed and returned the lease renewal documents. Could you confirm receipt?\n\nThanks,\nSarah",
            "is_reply": True,
        },
    ],
})

# === 6. HVAC FAILURE — Kevin Lee (78 Pine Road, Unit 303) ===
STORYLINES.append({
    "id": "hvac_kevin",
    "thread_subject": "AC not working - Unit 303, 78 Pine Road",
    "emails": [
        {
            "batch": "day1",
            "from_name": "Kevin Lee",
            "from_email": "kevin.lee.renter@gmail.com",
            "subject": "AC not working - Unit 303, 78 Pine Road",
            "body": "Hi,\n\nThe air conditioning in my unit (303, 78 Pine Road) stopped working sometime overnight. It's blowing warm air regardless of the thermostat setting. The temperature inside is already 87\u00b0F and climbing.\n\nI've tried resetting the thermostat and checking the breaker \u2014 everything looks fine on my end. Could you please send someone to look at it today if possible?\n\nThanks,\nKevin Lee\nUnit 303",
            "is_reply": False,
        },
        {
            "batch": "day2",
            "from_name": "Ace HVAC Services",
            "from_email": "ace.hvac.quotes@gmail.com",
            "subject": "Re: AC not working - Unit 303, 78 Pine Road",
            "body": "Hi,\n\nWe've scheduled a technician to visit Unit 303 at 78 Pine Road tomorrow between 10 AM and 12 PM. Based on the symptoms described (blowing warm air, thermostat unresponsive), it could be a refrigerant issue or a compressor problem.\n\nPlease make sure someone is home to let our tech in.\n\nRegards,\nTom Nguyen\nAce HVAC Services\n(555) 456-7890",
            "is_reply": True,
        },
        {
            "batch": "day3",
            "from_name": "Ace HVAC Services",
            "from_email": "ace.hvac.quotes@gmail.com",
            "subject": "Re: AC not working - Unit 303, 78 Pine Road",
            "body": "Hi,\n\nOur technician visited Unit 303 today. The diagnosis is a failed compressor. The unit is 11 years old and the compressor has reached end of life.\n\nQuote #HVAC-3301:\n- Compressor replacement (Copeland scroll, 2.5 ton): $1,450.00\n- Labour (5 hrs @ $110/hr): $550.00\n- Refrigerant recharge (R-410A): $185.00\n- Total: $2,185.00\n\nAlternative: Full unit replacement (recommended given age): $4,200.00 installed.\n\nPlease let us know how you'd like to proceed.\n\nTom Nguyen\nAce HVAC Services",
            "is_reply": True,
        },
        {
            "batch": "day4",
            "from_name": "Ace HVAC Services",
            "from_email": "ace.hvac.quotes@gmail.com",
            "subject": "Invoice - AC compressor replacement, Unit 303, 78 Pine Road",
            "body": "Hi,\n\nThe compressor replacement at Unit 303, 78 Pine Road has been completed. The AC is now cooling properly and all readings are within spec.\n\nInvoice #HVAC-3302\nCompressor (Copeland scroll, 2.5 ton): $1,450.00\nLabour (4.5 hrs @ $110/hr): $495.00\nRefrigerant recharge: $185.00\nTotal: $2,130.00\n\nPayment due within 30 days.\n\nTom Nguyen\nAce HVAC Services",
            "is_reply": False,
        },
    ],
})

# === 7. PEST CONTROL — Nathan Baker (103 Birch Court, Unit 201) ===
STORYLINES.append({
    "id": "pest_nathan",
    "thread_subject": "Roach problem - Unit 201, 103 Birch Court",
    "emails": [
        {
            "batch": "history",
            "from_name": "Nathan Baker",
            "from_email": "n.baker.renter@gmail.com",
            "subject": "Roach problem - Unit 201, 103 Birch Court",
            "body": "Hi,\n\nI've been seeing cockroaches in my kitchen for the past week. I found several in the cabinet under the sink and a couple near the stove. I've tried store-bought traps but they're not making a dent.\n\nCould you please arrange for professional pest control?\n\nThanks,\nNathan Baker\nUnit 201, 103 Birch Court",
            "is_reply": False,
        },
        {
            "batch": "history",
            "from_name": "Sunrise Pest Control",
            "from_email": "sunrise.pest.quotes@gmail.com",
            "subject": "Re: Roach problem - Unit 201, 103 Birch Court",
            "body": "Hi,\n\nWe treated Unit 201 at 103 Birch Court today. We applied gel bait in the kitchen and bathroom, and did a perimeter spray. The tenant should see a significant reduction within 5-7 days.\n\nInvoice #SPC-1190: $175.00\n\nIf the problem persists after 2 weeks, we'll do a follow-up treatment at no extra charge.\n\nBest,\nLisa Tran\nSunrise Pest Control",
            "is_reply": True,
        },
        {
            "batch": "day2",
            "from_name": "Nathan Baker",
            "from_email": "n.baker.renter@gmail.com",
            "subject": "Re: Roach problem - Unit 201, 103 Birch Court",
            "body": "Hi,\n\nI'm sorry to report that the roaches are back. It got better for about a week after the treatment but now I'm seeing them again, mostly at night in the kitchen. I think they might be coming through the wall from the unit next door.\n\nCan we get another treatment? This time maybe they should check the adjacent units too.\n\nThanks,\nNathan\nUnit 201",
            "is_reply": True,
        },
        {
            "batch": "day3",
            "from_name": "Sunrise Pest Control",
            "from_email": "sunrise.pest.quotes@gmail.com",
            "subject": "Re: Roach problem - Unit 201, 103 Birch Court",
            "body": "Hi,\n\nWe can schedule a follow-up treatment for Unit 201 and the adjacent units (202, 301, 302) at 103 Birch Court. Since this is a recurring issue, we recommend a more aggressive approach \u2014 full crack-and-crevice treatment plus boric acid dust in wall voids.\n\nWe have availability this Friday. The multi-unit treatment will be $425.00.\n\nPlease confirm and we'll get it on the schedule.\n\nLisa Tran\nSunrise Pest Control",
            "is_reply": True,
        },
        {
            "batch": "day4",
            "from_name": "Sunrise Pest Control",
            "from_email": "sunrise.pest.quotes@gmail.com",
            "subject": "Invoice - Pest treatment, 103 Birch Court (multiple units)",
            "body": "Hi,\n\nWe completed the pest treatment at 103 Birch Court today. Units 201, 202, 301, and 302 were all treated with crack-and-crevice application and boric acid dust.\n\nInvoice #SPC-1204\nMulti-unit treatment (4 units): $425.00\n\nWe recommend a follow-up inspection in 3 weeks. If any activity persists, the next treatment is included at no charge.\n\nLisa Tran\nSunrise Pest Control",
            "is_reply": False,
        },
    ],
})

# === 8. NOISE COMPLAINT — 55 Walnut Drive ===
# Lauren complains, Brandon responds separately (no cross-tenant thread)
STORYLINES.append({
    "id": "noise_walnut_lauren",
    "thread_subject": "Noise complaint - Unit 2A, 55 Walnut Drive",
    "emails": [
        {
            "batch": "history",
            "from_name": "Lauren Turner",
            "from_email": "l.turner.tenant@gmail.com",
            "subject": "Noise complaint - Unit 2A, 55 Walnut Drive",
            "body": "Hi,\n\nI'm writing to complain about excessive noise from the unit above me (2A). There was very loud music playing until well past midnight last Saturday. I have to be up at 6 AM for work and this made it impossible to sleep.\n\nCould you please remind the tenant about quiet hours?\n\nThank you,\nLauren Turner\nUnit 1B, 55 Walnut Drive",
            "is_reply": False,
        },
        {
            "batch": "day1",
            "from_name": "Lauren Turner",
            "from_email": "l.turner.tenant@gmail.com",
            "subject": "Re: Noise complaint - Unit 2A, 55 Walnut Drive",
            "body": "Hi,\n\nI'm writing again because the noise from Unit 2A happened again last night. Loud music and what sounded like a party until 2 AM. I knocked on the door twice but got no answer.\n\nThis is the second time in two weeks. I really need this to be addressed. I shouldn't have to wear earplugs in my own apartment.\n\nLauren Turner\nUnit 1B",
            "is_reply": True,
        },
        {
            "batch": "day4",
            "from_name": "Lauren Turner",
            "from_email": "l.turner.tenant@gmail.com",
            "subject": "Re: Noise complaint - Unit 2A, 55 Walnut Drive",
            "body": "Hi,\n\nJust wanted to let you know it's been quiet the past few nights. Whatever you said to the tenant in 2A seems to have worked. Thank you for handling it.\n\nLauren\nUnit 1B",
            "is_reply": True,
        },
    ],
})

STORYLINES.append({
    "id": "noise_walnut_brandon",
    "thread_subject": "About the noise complaint - Unit 2A, 55 Walnut Drive",
    "emails": [
        {
            "batch": "day2",
            "from_name": "Brandon Phillips",
            "from_email": "b.phillips.apt@gmail.com",
            "subject": "About the noise complaint - Unit 2A, 55 Walnut Drive",
            "body": "Hi,\n\nI got your message about the noise complaint. I want to apologize \u2014 my brother was visiting from out of town and things got louder than I intended. It was a one-time thing and it won't happen again.\n\nI'll be more mindful of the volume going forward, especially after 10 PM.\n\nSorry for the trouble.\n\nBrandon Phillips\nUnit 2A",
            "is_reply": False,
        },
    ],
})

# === 9. MOVE-OUT — Emily Davis (72 Ridgeline Terrace) ===
STORYLINES.append({
    "id": "moveout_emily",
    "thread_subject": "30-day move-out notice - 72 Ridgeline Terrace",
    "emails": [
        {
            "batch": "history",
            "from_name": "Emily Davis",
            "from_email": "emily.davis.lease@gmail.com",
            "subject": "30-day move-out notice - 72 Ridgeline Terrace",
            "body": "Hi,\n\nI'm writing to provide my formal 30-day notice to vacate 72 Ridgeline Terrace. I've accepted a job in another city and will need to move by the end of next month.\n\nI've loved living here and have taken great care of the property. Please let me know what the move-out process looks like \u2014 inspection, cleaning requirements, key return, etc.\n\nThank you,\nEmily Davis",
            "is_reply": False,
        },
        {
            "batch": "day1",
            "from_name": "Emily Davis",
            "from_email": "emily.davis.lease@gmail.com",
            "subject": "Re: 30-day move-out notice - 72 Ridgeline Terrace",
            "body": "Hi,\n\nFollowing up on my move-out notice. Could we schedule the move-out inspection for the last Saturday of the month? That would give me time to finish cleaning after I move my furniture out on Friday.\n\nAlso, should I arrange for a professional carpet cleaning or is that handled by management?\n\nThanks,\nEmily",
            "is_reply": True,
        },
        {
            "batch": "day3",
            "from_name": "Emily Davis",
            "from_email": "emily.davis.lease@gmail.com",
            "subject": "Re: 30-day move-out notice - 72 Ridgeline Terrace",
            "body": "Hi,\n\nPerfect, Saturday works great for the inspection. I'll have the place cleaned and ready by 10 AM. I'll drop the keys off at your office afterward.\n\nThanks for everything,\nEmily",
            "is_reply": True,
        },
        {
            "batch": "month1",
            "from_name": "Emily Davis",
            "from_email": "emily.davis.lease@gmail.com",
            "subject": "Re: 30-day move-out notice - 72 Ridgeline Terrace",
            "body": "Hi,\n\nI moved out last week and dropped the keys off as planned. Could you let me know the timeline for the security deposit return? My new address for the check is:\n\nEmily Davis\n1847 Oakmont Drive, Apt 4\nPortland, OR 97205\n\nThank you,\nEmily",
            "is_reply": True,
        },
    ],
})

# === 10. MOLD — Jonathan Edwards (18 Spruce Way, Unit 201) ===
STORYLINES.append({
    "id": "mold_jonathan",
    "thread_subject": "Mold in bathroom - Unit 201, 18 Spruce Way",
    "emails": [
        {
            "batch": "day2",
            "from_name": "Jonathan Edwards",
            "from_email": "jon.edwards.apt@gmail.com",
            "subject": "Mold in bathroom - Unit 201, 18 Spruce Way",
            "body": "Hi,\n\nI've noticed black mold growing along the ceiling in my bathroom (Unit 201, 18 Spruce Way). It's spreading from the corner above the shower. The exhaust fan doesn't seem to be working properly \u2014 it barely pulls any air.\n\nI'm concerned about health effects. My wife has been having allergy symptoms that started around the same time I first noticed the mold.\n\nCould you please have someone inspect this as soon as possible?\n\nThanks,\nJonathan Edwards\nUnit 201",
            "is_reply": False,
        },
        {
            "batch": "day3",
            "from_name": "EcoMold Remediation",
            "from_email": "ecomold.remediation@gmail.com",
            "subject": "Re: Mold in bathroom - Unit 201, 18 Spruce Way",
            "body": "Hi,\n\nWe've scheduled an inspection for Unit 201 at 18 Spruce Way for tomorrow at 2 PM. Our inspector will assess the extent of the mold growth, check moisture levels in the walls, and test the exhaust fan.\n\nIf remediation is needed, we'll provide a detailed quote on-site.\n\nPlease ensure the bathroom is accessible and any personal items are moved away from the affected area.\n\nRegards,\nCarla Diaz\nEcoMold Remediation\n(555) 678-3456",
            "is_reply": True,
        },
        {
            "batch": "day4",
            "from_name": "EcoMold Remediation",
            "from_email": "ecomold.remediation@gmail.com",
            "subject": "Re: Mold in bathroom - Unit 201, 18 Spruce Way",
            "body": "Hi,\n\nFollowing our inspection of Unit 201 at 18 Spruce Way, here are our findings:\n\n- Black mold (likely Stachybotrys) present on ~8 sq ft of ceiling\n- Moisture levels elevated in ceiling drywall (28% \u2014 normal is under 15%)\n- Exhaust fan motor is failing \u2014 pulling only 15 CFM vs rated 80 CFM\n- No mold detected in wall cavities (good news)\n\nRecommended remediation:\n- Remove and replace affected drywall section\n- HEPA vacuum and antimicrobial treatment\n- Replace exhaust fan\n- Apply mold-resistant paint\n\nQuote #EM-0445: $1,850.00\nTimeline: 1 day for remediation + 1 day for drywall/paint to cure\n\nThe tenant should avoid using the bathroom during remediation. We can start as early as next Monday.\n\nCarla Diaz\nEcoMold Remediation",
            "is_reply": True,
        },
        {
            "batch": "month1",
            "from_name": "Jonathan Edwards",
            "from_email": "jon.edwards.apt@gmail.com",
            "subject": "Re: Mold in bathroom - Unit 201, 18 Spruce Way",
            "body": "Hi,\n\nThe mold remediation was completed last week and everything looks great. The new exhaust fan is much more powerful. My wife's allergy symptoms have improved too.\n\nThank you for handling this quickly.\n\nJonathan\nUnit 201",
            "is_reply": True,
        },
    ],
})

# === 11. PARKING DISPUTE — 7 Ash Place ===
# Patrick complains, Tiffany emails separately to apologize (no cross-tenant thread)
STORYLINES.append({
    "id": "parking_ash_patrick",
    "thread_subject": "Someone in my parking spot - 7 Ash Place",
    "emails": [
        {
            "batch": "history",
            "from_name": "Patrick Reed",
            "from_email": "p.reed.apt@gmail.com",
            "subject": "Someone in my parking spot - 7 Ash Place",
            "body": "Hi,\n\nI came home tonight and there's a silver Honda Civic parked in my assigned spot (A1) at 7 Ash Place. No note, no permit visible. I had to park on the street.\n\nCould you please look into this and remind residents about assigned parking?\n\nThanks,\nPatrick Reed\nUnit A1",
            "is_reply": False,
        },
        {
            "batch": "day1",
            "from_name": "Patrick Reed",
            "from_email": "p.reed.apt@gmail.com",
            "subject": "Re: Someone in my parking spot - 7 Ash Place",
            "body": "Hi,\n\nIt happened again. Same silver Honda in my spot. This is the second time this week. I left a note on the windshield last time but clearly that didn't work.\n\nCan you please send a notice to all residents? If it happens again I'd like to have the car towed.\n\nPatrick\nUnit A1",
            "is_reply": True,
        },
    ],
})

STORYLINES.append({
    "id": "parking_ash_tiffany",
    "thread_subject": "Sorry about the parking situation - 7 Ash Place",
    "emails": [
        {
            "batch": "day2",
            "from_name": "Tiffany Cook",
            "from_email": "tiffany.cook.lease@gmail.com",
            "subject": "Sorry about the parking situation - 7 Ash Place",
            "body": "Hi,\n\nI think I owe you an apology. The silver Honda that's been in spot A1 is my sister's car. She's been visiting me this week and I didn't realize she was parking in the wrong spot. I thought A1 was a visitor space.\n\nI've told her to park on the street from now on. It won't happen again. Please apologize to the tenant in A1 for me.\n\nTiffany Cook\nUnit A2",
            "is_reply": False,
        },
    ],
})

# === 12. BROKEN APPLIANCE — James Smith (14 Birchwood Lane) ===
STORYLINES.append({
    "id": "appliance_james",
    "thread_subject": "Dishwasher broken - 14 Birchwood Lane",
    "emails": [
        {
            "batch": "history",
            "from_name": "James Smith",
            "from_email": "james.smith.tenant@gmail.com",
            "subject": "Dishwasher broken - 14 Birchwood Lane",
            "body": "Hi,\n\nThe dishwasher at 14 Birchwood Lane stopped draining about a week ago. It fills with water and runs the cycle but when it's done there's standing water at the bottom. I've cleaned the filter and checked for clogs but no luck.\n\nCould you arrange for a repair?\n\nThanks,\nJames Smith",
            "is_reply": False,
        },
        {
            "batch": "day1",
            "from_name": "James Smith",
            "from_email": "james.smith.tenant@gmail.com",
            "subject": "Re: Dishwasher broken - 14 Birchwood Lane",
            "body": "Hi,\n\nJust following up on the dishwasher \u2014 it's been two weeks now and I haven't heard anything. I've been hand-washing everything which is fine but I'd like to get this resolved when possible.\n\nAny update?\n\nJames",
            "is_reply": True,
        },
        {
            "batch": "day2",
            "from_name": "Premier Appliance Repair",
            "from_email": "premier.appliance.svc@gmail.com",
            "subject": "Re: Dishwasher broken - 14 Birchwood Lane",
            "body": "Hi,\n\nWe've scheduled a technician to look at the dishwasher at 14 Birchwood Lane tomorrow between 1-3 PM. Based on the description (not draining), it's likely the drain pump motor or a blocked drain hose.\n\nPlease ensure access to the kitchen.\n\nRegards,\nPremier Appliance Repair\n(555) 345-6789",
            "is_reply": True,
        },
        {
            "batch": "day3",
            "from_name": "Premier Appliance Repair",
            "from_email": "premier.appliance.svc@gmail.com",
            "subject": "Invoice - Dishwasher repair, 14 Birchwood Lane",
            "body": "Hi,\n\nThe dishwasher at 14 Birchwood Lane has been repaired. The drain pump motor had seized. We replaced it and tested several cycles \u2014 all draining properly now.\n\nInvoice #PAR-0567\nDrain pump motor: $89.00\nLabour (1.5 hrs @ $85/hr): $127.50\nTotal: $216.50\n\nPayment due within 30 days.\n\nPremier Appliance Repair",
            "is_reply": False,
        },
    ],
})

# === 13. SECURITY / LOCK — 12 Oak Street ===
# Two tenants report the same lock issue independently (cluster scenario)
STORYLINES.append({
    "id": "lock_oak_joshua",
    "thread_subject": "Building entrance lock broken - 12 Oak Street",
    "emails": [
        {
            "batch": "history",
            "from_name": "Joshua Wright",
            "from_email": "j.wright.renter@gmail.com",
            "subject": "Building entrance lock broken - 12 Oak Street",
            "body": "Hi,\n\nThe electronic lock on the main entrance at 12 Oak Street isn't working properly. My key fob doesn't register about half the time and I've seen the door propped open with a rock, which is a security concern.\n\nCould you have someone look at it?\n\nThanks,\nJoshua Wright\nUnit 2A",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "lock_oak_megan",
    "thread_subject": "Front door lock not working - 12 Oak Street",
    "emails": [
        {
            "batch": "day1",
            "from_name": "Megan Scott",
            "from_email": "megan.scott.unit@gmail.com",
            "subject": "Front door lock not working - 12 Oak Street",
            "body": "Hi,\n\nThe front door lock at 12 Oak Street is getting worse. This morning it wouldn't read anyone's fob at all. Several of us were stuck outside until someone opened it from inside.\n\nThis is a safety issue, especially at night.\n\nMegan Scott\nUnit 2B",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "lock_oak_contractor",
    "thread_subject": "Lock repair request - 12 Oak Street",
    "emails": [
        {
            "batch": "day2",
            "from_name": "SafeGuard Locksmith",
            "from_email": "safeguard.locksmith@gmail.com",
            "subject": "Lock repair request - 12 Oak Street",
            "body": "Hi,\n\nWe can send a technician to 12 Oak Street tomorrow morning to diagnose the electronic lock issue. If it's the reader unit, we carry common replacements on our truck and can likely fix it same-day.\n\nService call: $75.00 (applied to repair if we proceed)\n\nPlease confirm.\n\nSafeGuard Locksmith\n(555) 789-0123",
            "is_reply": False,
        },
        {
            "batch": "day3",
            "from_name": "SafeGuard Locksmith",
            "from_email": "safeguard.locksmith@gmail.com",
            "subject": "Invoice - Lock repair, 12 Oak Street",
            "body": "Hi,\n\nWe've completed the lock repair at 12 Oak Street. The RFID reader module had failed. We replaced it and reprogrammed all existing fobs. Everything is working properly.\n\nInvoice #SGL-0334\nRFID reader module: $220.00\nLabour (2 hrs @ $90/hr): $180.00\nFob reprogramming (12 fobs): $60.00\nTotal: $460.00\n\nPayment due within 30 days.\n\nSafeGuard Locksmith",
            "is_reply": True,
        },
    ],
})

# === 14. WATER HEATER — Maria Garcia (88 Sunset Drive) ===
STORYLINES.append({
    "id": "waterheater_maria",
    "thread_subject": "No hot water - 88 Sunset Drive",
    "emails": [
        {
            "batch": "day2",
            "from_name": "Maria Garcia",
            "from_email": "maria.garcia.apt4b@gmail.com",
            "subject": "No hot water - 88 Sunset Drive",
            "body": "Hi,\n\nI woke up this morning to no hot water at 88 Sunset Drive. The water heater pilot light appears to be out and I can't get it to relight \u2014 the igniter clicks but nothing catches.\n\nCould you please send someone to look at it? Cold showers are not fun!\n\nThanks,\nMaria Garcia",
            "is_reply": False,
        },
        {
            "batch": "day3",
            "from_name": "ProFix Contractors",
            "from_email": "profix.contractors@gmail.com",
            "subject": "Re: No hot water - 88 Sunset Drive",
            "body": "Hi,\n\nWe visited 88 Sunset Drive today. The water heater thermocouple has failed, which is why the pilot won't stay lit. The unit is 14 years old.\n\nWe can replace the thermocouple ($45 part + $95 labour = $140 total) but given the age of the unit, you may want to consider a full replacement. A new 50-gallon gas water heater installed would be approximately $1,200.\n\nLet us know which option you prefer.\n\nProFix Contractors\n(555) 567-8901",
            "is_reply": True,
        },
        {
            "batch": "day4",
            "from_name": "ProFix Contractors",
            "from_email": "profix.contractors@gmail.com",
            "subject": "Invoice - Water heater repair, 88 Sunset Drive",
            "body": "Hi,\n\nThermocouple replacement at 88 Sunset Drive is complete. Hot water is restored.\n\nInvoice #PF-7823\nThermocouple: $45.00\nLabour (1 hr): $95.00\nTotal: $140.00\n\nPayment due within 30 days.\n\nProFix Contractors",
            "is_reply": False,
        },
    ],
})

# === 15. LEASE / PET QUESTION — Kayla Adams (12 Oak Street, 3B) ===
STORYLINES.append({
    "id": "pet_kayla",
    "thread_subject": "Pet policy question - Unit 3B, 12 Oak Street",
    "emails": [
        {
            "batch": "history",
            "from_name": "Kayla Adams",
            "from_email": "kayla.adams.tenant@gmail.com",
            "subject": "Pet policy question - Unit 3B, 12 Oak Street",
            "body": "Hi,\n\nI'm thinking about getting a dog and wanted to check the pet policy for 12 Oak Street. My lease mentions a pet deposit but doesn't specify the amount or any breed/size restrictions. Could you clarify?\n\nI'm looking at a medium-sized Labrador mix, about 45 lbs.\n\nThanks,\nKayla Adams\nUnit 3B",
            "is_reply": False,
        },
        {
            "batch": "day1",
            "from_name": "Kayla Adams",
            "from_email": "kayla.adams.tenant@gmail.com",
            "subject": "Re: Pet policy question - Unit 3B, 12 Oak Street",
            "body": "Hi,\n\nJust following up on my pet policy question. I found a dog I'd really like to adopt but the shelter needs an answer by the end of the week. Could you let me know about the deposit amount and any restrictions?\n\nThanks,\nKayla",
            "is_reply": True,
        },
        {
            "batch": "day3",
            "from_name": "Kayla Adams",
            "from_email": "kayla.adams.tenant@gmail.com",
            "subject": "Re: Pet policy question - Unit 3B, 12 Oak Street",
            "body": "Hi,\n\nThank you for the info! $300 pet deposit and $25/month pet rent is reasonable. I'll go ahead and adopt the dog. I can drop off the deposit check this week.\n\nHer name is Luna \u2014 she's very well-behaved, I promise!\n\nThanks,\nKayla",
            "is_reply": True,
        },
    ],
})

# === 16. ROOF LEAK — William Anderson (267 Coventry Circle) ===
STORYLINES.append({
    "id": "roof_william",
    "thread_subject": "Roof leak during rain - 267 Coventry Circle",
    "emails": [
        {
            "batch": "history",
            "from_name": "William Anderson",
            "from_email": "william.a.tenant@gmail.com",
            "subject": "Roof leak during rain - 267 Coventry Circle",
            "body": "Hi,\n\nDuring the heavy rain last week, I noticed water dripping from the ceiling in the upstairs hallway at 267 Coventry Circle. It only happens when it rains hard. I've put a bucket down but the ceiling has a brownish stain now.\n\nCould you have the roof inspected?\n\nThanks,\nWilliam Anderson",
            "is_reply": False,
        },
        {
            "batch": "history",
            "from_name": "Metro Roofing Inc.",
            "from_email": "metro.roofing.bids@gmail.com",
            "subject": "Re: Roof leak during rain - 267 Coventry Circle",
            "body": "Hi,\n\nWe inspected the roof at 267 Coventry Circle today. We found several cracked shingles and deteriorated flashing around the chimney. The leak is coming from the flashing area.\n\nWe'll have a detailed repair quote to you within 48 hours.\n\nRegards,\nJim Kowalski\nMetro Roofing Inc.",
            "is_reply": True,
        },
        {
            "batch": "day2",
            "from_name": "Metro Roofing Inc.",
            "from_email": "metro.roofing.bids@gmail.com",
            "subject": "Re: Roof leak during rain - 267 Coventry Circle",
            "body": "Hi,\n\nHere's our quote for the roof repair at 267 Coventry Circle:\n\nQuote #MR-2024-156\n- Replace cracked shingles (approx 40 sq ft): $320.00\n- Remove and replace chimney flashing: $480.00\n- Seal and waterproof affected area: $150.00\n- Labour (6 hrs @ $95/hr): $570.00\n- Total: $1,520.00\n\nWeather permitting, we can schedule the work for early next week.\n\nJim Kowalski\nMetro Roofing Inc.",
            "is_reply": True,
        },
        {
            "batch": "day4",
            "from_name": "Metro Roofing Inc.",
            "from_email": "metro.roofing.bids@gmail.com",
            "subject": "Invoice - Roof repair, 267 Coventry Circle",
            "body": "Hi,\n\nRoof repair at 267 Coventry Circle is complete. We replaced the damaged shingles, installed new chimney flashing, and sealed the entire area. The next rain should confirm the fix but we're confident the leak is resolved.\n\nInvoice #MR-2024-157\nMaterials: $950.00\nLabour (5.5 hrs): $522.50\nTotal: $1,472.50\n\nPayment due within 30 days. 1-year warranty on all work.\n\nJim Kowalski\nMetro Roofing Inc.",
            "is_reply": False,
        },
    ],
})

# === 17. GARBAGE DISPOSAL — Michael Brown (156 Magnolia Court) ===
STORYLINES.append({
    "id": "disposal_michael",
    "thread_subject": "Garbage disposal jammed - 156 Magnolia Court",
    "emails": [
        {
            "batch": "history",
            "from_name": "Michael Brown",
            "from_email": "mbrown.tenant@gmail.com",
            "subject": "Garbage disposal jammed - 156 Magnolia Court",
            "body": "Hi,\n\nThe garbage disposal at 156 Magnolia Court is jammed. It makes a humming noise when I flip the switch but the blades won't turn. I tried the reset button and using an Allen wrench at the bottom but it's stuck solid.\n\nCould you send someone to fix or replace it?\n\nThanks,\nMichael Brown",
            "is_reply": False,
        },
        {
            "batch": "history",
            "from_name": "QuickRepair LLC",
            "from_email": "quickrepair.quotes@gmail.com",
            "subject": "Re: Garbage disposal jammed - 156 Magnolia Court",
            "body": "Hi,\n\nWe replaced the garbage disposal at 156 Magnolia Court. The old unit had a seized motor. New unit is a 1/2 HP InSinkErator.\n\nInvoice #QR-4455\nDisposal unit: $129.00\nLabour (1 hr): $85.00\nTotal: $214.00\n\nQuickRepair LLC",
            "is_reply": True,
        },
    ],
})

# === 18. WINDOW REPAIR — Robert Wilson (445 Lakeshore Blvd) ===
STORYLINES.append({
    "id": "window_robert",
    "thread_subject": "Cracked window - 445 Lakeshore Blvd",
    "emails": [
        {
            "batch": "history",
            "from_name": "Robert Wilson",
            "from_email": "rwilson.apt@gmail.com",
            "subject": "Cracked window - 445 Lakeshore Blvd",
            "body": "Hi,\n\nI noticed a crack in the living room window at 445 Lakeshore Blvd. It looks like a stress crack \u2014 I didn't hit it or anything. It's about 8 inches long and I can feel cold air coming through.\n\nCould you arrange for a replacement?\n\nThanks,\nRobert Wilson",
            "is_reply": False,
        },
        {
            "batch": "day2",
            "from_name": "ClearView Glass & Mirror",
            "from_email": "clearview.glass@gmail.com",
            "subject": "Re: Cracked window - 445 Lakeshore Blvd",
            "body": "Hi,\n\nWe measured the window at 445 Lakeshore Blvd. It's a standard double-pane unit, 36\" x 48\". We'll need to order the glass \u2014 should arrive in 3-5 business days.\n\nQuote: $385.00 (glass + installation)\n\nWe'll contact you to schedule installation once the glass arrives.\n\nClearView Glass & Mirror\n(555) 234-5678",
            "is_reply": True,
        },
        {
            "batch": "month1",
            "from_name": "ClearView Glass & Mirror",
            "from_email": "clearview.glass@gmail.com",
            "subject": "Invoice - Window replacement, 445 Lakeshore Blvd",
            "body": "Hi,\n\nWindow replacement at 445 Lakeshore Blvd is complete.\n\nInvoice #CV-0891\nDouble-pane glass (36\" x 48\"): $265.00\nLabour (1.5 hrs): $120.00\nTotal: $385.00\n\nPayment due within 30 days.\n\nClearView Glass & Mirror",
            "is_reply": False,
        },
    ],
})

# === 19. LEASE RENEWAL — Amanda Allen (231 Elm Blvd, Unit 2) ===
STORYLINES.append({
    "id": "lease_amanda",
    "thread_subject": "Lease renewal - Unit 2, 231 Elm Blvd",
    "emails": [
        {
            "batch": "history",
            "from_name": "Amanda Allen",
            "from_email": "a.allen.lease@gmail.com",
            "subject": "Lease renewal - Unit 2, 231 Elm Blvd",
            "body": "Hi,\n\nI received the lease renewal notice for Unit 2 at 231 Elm Blvd. I'd like to renew but I have a question \u2014 is it possible to switch to a month-to-month arrangement? My company might be transferring me in 6 months and I don't want to be locked into a full year.\n\nThanks,\nAmanda Allen\nUnit 2",
            "is_reply": False,
        },
        {
            "batch": "day3",
            "from_name": "Amanda Allen",
            "from_email": "a.allen.lease@gmail.com",
            "subject": "Re: Lease renewal - Unit 2, 231 Elm Blvd",
            "body": "Hi,\n\nThank you for the month-to-month option. The $100/month premium is a bit steep but I understand. I'll go ahead with the standard 12-month renewal for now. If the transfer comes through, I'll give proper notice.\n\nPlease send the paperwork.\n\nAmanda",
            "is_reply": True,
        },
    ],
})

# === 20. FIRE ALARM TESTING — 400 Willow Terrace ===
STORYLINES.append({
    "id": "firealarm_willow",
    "thread_subject": "Annual fire alarm testing - 400 Willow Terrace",
    "emails": [
        {
            "batch": "history",
            "from_name": "Redline Fire Safety",
            "from_email": "redline.firesafety@gmail.com",
            "subject": "Annual fire alarm testing - 400 Willow Terrace",
            "body": "Hi,\n\nThis is to confirm that we completed the annual fire alarm system inspection and testing at 400 Willow Terrace. All smoke detectors, pull stations, and the main panel are functioning properly.\n\nTwo smoke detectors in the hallways were replaced (batteries dead).\n\nInvoice #RFS-0223\nAnnual inspection: $350.00\nReplacement detectors (2x): $45.00\nTotal: $395.00\n\nNext inspection due in 12 months.\n\nRedline Fire Safety",
            "is_reply": False,
        },
    ],
})

# === 21. LANDSCAPING — GreenLeaf quarterly ===
STORYLINES.append({
    "id": "landscaping_quarterly",
    "thread_subject": "Quarterly landscaping service - multiple properties",
    "emails": [
        {
            "batch": "history",
            "from_name": "GreenLeaf Landscaping",
            "from_email": "greenleaf.quotes@gmail.com",
            "subject": "Quarterly landscaping service - multiple properties",
            "body": "Hi,\n\nThis is a reminder that our quarterly landscaping service is coming up next week. We'll be servicing the following properties:\n\n- 92 Hawthorn Gardens\n- 103 Birch Court\n- 400 Willow Terrace\n- 7 Ash Place\n\nServices include: lawn mowing, hedge trimming, leaf removal, and flower bed maintenance.\n\nQuarterly rate: $1,200.00 (4 properties)\n\nPlease confirm the schedule works for you.\n\nGreenLeaf Landscaping",
            "is_reply": False,
        },
        {
            "batch": "history",
            "from_name": "GreenLeaf Landscaping",
            "from_email": "greenleaf.quotes@gmail.com",
            "subject": "Invoice - Quarterly landscaping service",
            "body": "Hi,\n\nQuarterly landscaping service has been completed at all four properties.\n\nInvoice #GL-Q2-2024\n4 properties x $300/property: $1,200.00\n\nPayment due within 30 days.\n\nGreenLeaf Landscaping",
            "is_reply": False,
        },
    ],
})

# === 22. DEREK COOPER — Extra rudeness (non-elevator) ===
STORYLINES.append({
    "id": "derek_hallway",
    "thread_subject": "Hallway light out AGAIN - 92 Hawthorn Gardens",
    "emails": [
        {
            "batch": "history",
            "from_name": "Derek Cooper",
            "from_email": "derek.cooper.apt@gmail.com",
            "subject": "Hallway light out AGAIN - 92 Hawthorn Gardens",
            "body": "The 3rd floor hallway light has been out for 4 days. FOUR DAYS. How hard is it to change a light bulb? I'm stumbling around in the dark every night trying to find my keys.\n\nThis is basic building maintenance. Get it done.\n\nDerek Cooper\nUnit 301",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "derek_trash",
    "thread_subject": "Trash situation is disgusting - 92 Hawthorn Gardens",
    "emails": [
        {
            "batch": "day1",
            "from_name": "Derek Cooper",
            "from_email": "derek.cooper.apt@gmail.com",
            "subject": "Trash situation is disgusting - 92 Hawthorn Gardens",
            "body": "The dumpster area is overflowing AGAIN. There are trash bags piled up outside the bin and it smells terrible. I saw a rat out there last night. A RAT.\n\nI don't know what I'm paying for at this point. Between the elevator, the hallway lights, and now this, the building is falling apart. Get the trash company to come more often or get a bigger dumpster.\n\nThis is a health hazard.\n\nDerek Cooper\nUnit 301",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "derek_laundry",
    "thread_subject": "Laundry room is a disaster - 92 Hawthorn Gardens",
    "emails": [
        {
            "batch": "day2",
            "from_name": "Derek Cooper",
            "from_email": "derek.cooper.apt@gmail.com",
            "subject": "Laundry room is a disaster - 92 Hawthorn Gardens",
            "body": "The laundry room is absolutely filthy. There's lint everywhere, one of the dryers has been broken for weeks, and someone left their wet clothes in a washer for what looks like days. It smells like mildew.\n\nI'm paying premium rent and I can't even do my laundry in a clean facility. This is embarrassing. Do you even have a cleaning service for this building?\n\nDerek Cooper\nUnit 301",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "derek_rent_threat",
    "thread_subject": "Considering my options - 92 Hawthorn Gardens",
    "emails": [
        {
            "batch": "month1",
            "from_name": "Derek Cooper",
            "from_email": "derek.cooper.apt@gmail.com",
            "subject": "Considering my options - 92 Hawthorn Gardens",
            "body": "I've been keeping a list of every maintenance issue, every delayed response, and every inconvenience I've experienced in this building over the past few months. The elevator alone has been broken twice. The hallway lights, the trash, the laundry room \u2014 it's a pattern of neglect.\n\nI'm seriously considering not renewing my lease. I've been looking at other buildings in the area and frankly the competition is offering better value.\n\nIf you want to keep me as a tenant, I expect to see significant improvements AND a rent reduction to compensate for the ongoing issues.\n\nDerek Cooper\nUnit 301",
            "is_reply": False,
        },
    ],
})

# === 23. ELECTRICAL — David Chen (203 Elm Street) ===
STORYLINES.append({
    "id": "electrical_david",
    "thread_subject": "Electrical outlet sparking - 203 Elm Street",
    "emails": [
        {
            "batch": "history",
            "from_name": "David Chen",
            "from_email": "david.chen.renter@gmail.com",
            "subject": "Electrical outlet sparking - 203 Elm Street",
            "body": "Hi,\n\nOne of the electrical outlets in my living room at 203 Elm Street sparked when I plugged in my laptop charger. The outlet also feels warm to the touch. I've stopped using it but I'm concerned about a fire hazard.\n\nCould you have an electrician look at it?\n\nThanks,\nDavid Chen",
            "is_reply": False,
        },
        {
            "batch": "history",
            "from_name": "City Electric Co.",
            "from_email": "cityelectric.bids@gmail.com",
            "subject": "Re: Electrical outlet sparking - 203 Elm Street",
            "body": "Hi,\n\nWe inspected the outlet at 203 Elm Street. The issue was a loose wire connection inside the outlet box causing arcing. We've replaced the outlet and tightened all connections in that circuit.\n\nWe also checked the adjacent outlets and found one more with a loose neutral wire \u2014 fixed that too.\n\nInvoice #CE-8834\nLabour (1.5 hrs @ $95/hr): $142.50\nMaterials (2 outlets): $24.00\nTotal: $166.50\n\nCity Electric Co.",
            "is_reply": True,
        },
    ],
})

# === 24. RENT CONFIRMATION — Jessica Martinez (19 Foxglove Way) ===
STORYLINES.append({
    "id": "rent_jessica",
    "thread_subject": "Rent payment confirmation - 19 Foxglove Way",
    "emails": [
        {
            "batch": "history",
            "from_name": "Jessica Martinez",
            "from_email": "jessica.m.renter@gmail.com",
            "subject": "Rent payment confirmation - 19 Foxglove Way",
            "body": "Hi,\n\nJust confirming that I sent this month's rent via bank transfer this morning. Could you confirm once it's received?\n\nThanks,\nJessica Martinez\n19 Foxglove Way",
            "is_reply": False,
        },
    ],
})

# === 25. CLEANING SERVICE — BrightStar ===
STORYLINES.append({
    "id": "cleaning_brightstar",
    "thread_subject": "Monthly common area cleaning - schedule confirmation",
    "emails": [
        {
            "batch": "history",
            "from_name": "BrightStar Cleaning Co.",
            "from_email": "brightstar.cleaning@gmail.com",
            "subject": "Monthly common area cleaning - schedule confirmation",
            "body": "Hi,\n\nThis is to confirm our monthly common area cleaning schedule for your properties:\n\n- 92 Hawthorn Gardens: 1st and 3rd Monday\n- 103 Birch Court: 1st and 3rd Tuesday\n- 55 Walnut Drive: 2nd and 4th Monday\n- 18 Spruce Way: 2nd and 4th Tuesday\n\nServices include: lobby mopping, stairwell cleaning, window washing (ground floor), and trash area sanitizing.\n\nMonthly rate: $800.00 (4 properties)\n\nPlease let us know if any changes are needed.\n\nBrightStar Cleaning Co.",
            "is_reply": False,
        },
    ],
})

# === 26. LEASE SIGNING — Christopher Thomas (45 Maple Ave, 1A) ===
STORYLINES.append({
    "id": "lease_christopher",
    "thread_subject": "Lease signing confirmation - Unit 1A, 45 Maple Avenue",
    "emails": [
        {
            "batch": "history",
            "from_name": "Christopher Thomas",
            "from_email": "c.thomas.renter@gmail.com",
            "subject": "Lease signing confirmation - Unit 1A, 45 Maple Avenue",
            "body": "Hi,\n\nJust confirming that I've signed and returned the lease for Unit 1A at 45 Maple Avenue. I also dropped off the security deposit check ($1,800) at your office today.\n\nLooking forward to moving in on the 1st!\n\nThanks,\nChristopher Thomas",
            "is_reply": False,
        },
    ],
})

# === 27. WATERPROOFING — TruSeal (basement at 78 Pine Road) ===
STORYLINES.append({
    "id": "waterproofing_pine",
    "thread_subject": "Basement waterproofing inspection - 78 Pine Road",
    "emails": [
        {
            "batch": "history",
            "from_name": "TruSeal Waterproofing",
            "from_email": "truseal.waterproof@gmail.com",
            "subject": "Basement waterproofing inspection - 78 Pine Road",
            "body": "Hi,\n\nFollowing our inspection of the basement at 78 Pine Road, we found minor seepage along the east wall foundation joint. Currently not severe but could worsen with heavy rain.\n\nWe recommend interior waterproofing membrane application on the affected wall section.\n\nQuote #TW-0567: $2,400.00\n\nThis includes a 5-year warranty against water intrusion.\n\nLet us know if you'd like to proceed.\n\nTruSeal Waterproofing",
            "is_reply": False,
        },
    ],
})


# ===================================================================
# CLUSTER SCENARIOS — multiple tenants independently report same issue
# The AI should recognize these are about the same problem and group them.
# ===================================================================

# --- DAY 2 CLUSTER: Garage door broken at 103 Birch Court ---
STORYLINES.append({
    "id": "garage_door_nathan",
    "thread_subject": "Garage door won't open - 103 Birch Court",
    "emails": [
        {
            "batch": "day2",
            "from_name": "Nathan Baker",
            "from_email": "n.baker.renter@gmail.com",
            "subject": "Garage door won't open - 103 Birch Court",
            "body": "Hi,\n\nThe garage door at 103 Birch Court is stuck and won't open. I pressed my remote several times but nothing happens. I can hear the motor trying to engage but the door doesn't move. I'm stuck and can't get my car out.\n\nCould you please send someone to look at it ASAP?\n\nThanks,\nNathan Baker\nUnit 201",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "garage_door_brittany",
    "thread_subject": "Can't get into the garage - 103 Birch Court",
    "emails": [
        {
            "batch": "day2",
            "from_name": "Brittany Carter",
            "from_email": "b.carter.lease@gmail.com",
            "subject": "Can't get into the garage - 103 Birch Court",
            "body": "Hi,\n\nI just got home from work and the garage door at 103 Birch Court won't open. My remote isn't working and neither is the keypad. I had to park on the street.\n\nIs anyone else having this problem? Please let me know when it will be fixed.\n\nThanks,\nBrittany Carter\nUnit 202",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "garage_door_andrew",
    "thread_subject": "Garage door issue - 103 Birch Court",
    "emails": [
        {
            "batch": "day2",
            "from_name": "Andrew Mitchell",
            "from_email": "andrew.m.tenant@gmail.com",
            "subject": "Garage door issue - 103 Birch Court",
            "body": "Hi,\n\nJust wanted to report that the garage door at 103 Birch Court seems to be broken. The motor makes a grinding noise but the door won't budge. I noticed Nathan from 201 was also trying to get it open this morning.\n\nPlease arrange a repair.\n\nThanks,\nAndrew Mitchell\nUnit 301",
            "is_reply": False,
        },
    ],
})

# --- DAY 3 CLUSTER: Hot water outage at 400 Willow Terrace ---
STORYLINES.append({
    "id": "hotwater_aaron",
    "thread_subject": "No hot water - Unit 4, 400 Willow Terrace",
    "emails": [
        {
            "batch": "day3",
            "from_name": "Aaron Stewart",
            "from_email": "aaron.s.tenant@gmail.com",
            "subject": "No hot water - Unit 4, 400 Willow Terrace",
            "body": "Hi,\n\nThere's no hot water in my unit this morning. The cold water works fine but the hot tap runs completely cold. Is this a building-wide issue or just my unit?\n\nThanks,\nAaron Stewart\nUnit 4",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "hotwater_danielle",
    "thread_subject": "Hot water not working - 400 Willow Terrace",
    "emails": [
        {
            "batch": "day3",
            "from_name": "Danielle Sanchez",
            "from_email": "d.sanchez.apt@gmail.com",
            "subject": "Hot water not working - 400 Willow Terrace",
            "body": "Hi,\n\nI don't have any hot water in Unit 5 at 400 Willow Terrace. I tried waiting 10 minutes but it stays ice cold. I need to shower before work so this is pretty urgent.\n\nPlease let me know what's going on.\n\nDanielle Sanchez\nUnit 5",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "hotwater_melissa",
    "thread_subject": "Cold water only - Unit 7, 400 Willow Terrace",
    "emails": [
        {
            "batch": "day3",
            "from_name": "Melissa Rogers",
            "from_email": "melissa.r.tenant@gmail.com",
            "subject": "Cold water only - Unit 7, 400 Willow Terrace",
            "body": "Hi,\n\nIs the hot water boiler broken? I have no hot water in Unit 7. I spoke to my neighbor Zachary and he said he doesn't have hot water either. Seems like it might be the whole building.\n\nCould you please look into this?\n\nThanks,\nMelissa Rogers\nUnit 7",
            "is_reply": False,
        },
    ],
})

# --- DAY 4 CLUSTER: Hallway lights out at 18 Spruce Way ---
STORYLINES.append({
    "id": "lights_eric",
    "thread_subject": "Hallway lights out - 18 Spruce Way",
    "emails": [
        {
            "batch": "day4",
            "from_name": "Eric Parker",
            "from_email": "eric.parker.unit@gmail.com",
            "subject": "Hallway lights out - 18 Spruce Way",
            "body": "Hi,\n\nAll the hallway lights on the 1st floor of 18 Spruce Way are out. It's completely dark when you come in the front entrance. I nearly tripped on the stairs this evening.\n\nCould you have someone check the breaker or replace the bulbs?\n\nThanks,\nEric Parker\nUnit 101",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "lights_amber",
    "thread_subject": "Dark hallways - 18 Spruce Way",
    "emails": [
        {
            "batch": "day4",
            "from_name": "Amber Evans",
            "from_email": "amber.evans.tenant@gmail.com",
            "subject": "Dark hallways - 18 Spruce Way",
            "body": "Hi,\n\nThe hallway lights are out on both the 1st and 2nd floors at 18 Spruce Way. It's been dark since I got home around 6 PM. I don't feel safe walking to my unit in the dark, especially at night.\n\nPlease fix this as soon as possible.\n\nAmber Evans\nUnit 102",
            "is_reply": False,
        },
    ],
})

# --- MONTH 1 CLUSTER: Heating issues at 78 Pine Road ---
STORYLINES.append({
    "id": "heating_matt",
    "thread_subject": "Heater not working - Unit 101, 78 Pine Road",
    "emails": [
        {
            "batch": "month1",
            "from_name": "Matthew Martin",
            "from_email": "matt.martin.tenant@gmail.com",
            "subject": "Heater not working - Unit 101, 78 Pine Road",
            "body": "Hi,\n\nThe heater in my unit (101) at 78 Pine Road isn't producing any heat. The thermostat is set to 72 but the apartment is freezing. I can see my breath inside.\n\nCould you please send someone? It's supposed to get down to 25\u00b0F tonight.\n\nThanks,\nMatt Martin\nUnit 101",
            "is_reply": False,
        },
    ],
})

STORYLINES.append({
    "id": "heating_stephanie",
    "thread_subject": "No heat in my apartment - 78 Pine Road",
    "emails": [
        {
            "batch": "month1",
            "from_name": "Stephanie Hall",
            "from_email": "s.hall.tenant@gmail.com",
            "subject": "No heat in my apartment - 78 Pine Road",
            "body": "Hi,\n\nI have no heat in Unit 404 at 78 Pine Road. The radiator is completely cold. I've been using a space heater but I'm worried about the pipes freezing if this isn't fixed soon.\n\nIs this affecting other units too?\n\nStephanie Hall\nUnit 404",
            "is_reply": False,
        },
    ],
})


# ===================================================================
# ROUTINE EMAILS — everyday filler, keyed by batch
# ===================================================================
ROUTINE_EMAILS = {
    "history": [
        {"from_name": "Linda Taylor", "from_email": "linda.taylor.apt@gmail.com", "subject": "Rent payment sent - 8 Whispering Pines Road", "body": "Hi,\n\nJust confirming rent was sent via e-transfer this morning.\n\nThanks,\nLinda Taylor"},
        {"from_name": "Aaron Stewart", "from_email": "aaron.s.tenant@gmail.com", "subject": "Maintenance request - light bulb, Unit 4, 400 Willow Terrace", "body": "Hi,\n\nThe light bulb in my hallway closet burned out. I know it's minor but it's one of those recessed fixtures I can't reach without a tall ladder. Could maintenance swap it out when they're in the building?\n\nThanks,\nAaron\nUnit 4"},
        {"from_name": "Stephanie Hall", "from_email": "s.hall.tenant@gmail.com", "subject": "Package delivery question - Unit 404, 78 Pine Road", "body": "Hi,\n\nI'm expecting a large package delivery this week. Is there a secure area where the delivery driver can leave it if I'm not home? I don't want it sitting in the lobby.\n\nThanks,\nStephanie Hall\nUnit 404"},
        {"from_name": "Brian Walker", "from_email": "brian.w.apt@gmail.com", "subject": "Rent payment confirmation - Unit 1, 231 Elm Blvd", "body": "Hi,\n\nJust confirming this month's rent was deposited today. Please confirm receipt.\n\nBrian Walker\nUnit 1"},
        {"from_name": "Samantha Perez", "from_email": "s.perez.apt@gmail.com", "subject": "Question about renter's insurance - Unit 302, 103 Birch Court", "body": "Hi,\n\nMy renter's insurance is up for renewal. Does the building have any preferred insurance providers or specific coverage requirements I should know about?\n\nThanks,\nSamantha Perez\nUnit 302"},
        {"from_name": "Amber Evans", "from_email": "amber.evans.tenant@gmail.com", "subject": "Visitor parking question - 18 Spruce Way", "body": "Hi,\n\nMy parents are visiting next weekend. Are there designated visitor parking spots or should they park on the street?\n\nThanks,\nAmber\nUnit 102"},
        {"from_name": "Crystal Bell", "from_email": "crystal.bell.apt@gmail.com", "subject": "Rent sent - Unit B2, 7 Ash Place", "body": "Hi,\n\nRent for this month has been sent via bank transfer.\n\nCrystal Bell\nUnit B2"},
        {"from_name": "Nicole King", "from_email": "nicole.king.apt@gmail.com", "subject": "Smoke detector beeping - Unit 4, 231 Elm Blvd", "body": "Hi,\n\nThe smoke detector in my bedroom has been chirping every 30 seconds. I think it needs a new battery but it's hardwired and I'm not sure how to open it. Could maintenance come swap the battery?\n\nThanks,\nNicole King\nUnit 4"},
        {"from_name": "Danielle Sanchez", "from_email": "d.sanchez.apt@gmail.com", "subject": "Mailbox key not working - Unit 5, 400 Willow Terrace", "body": "Hi,\n\nMy mailbox key has been sticking lately and today it wouldn't turn at all. Could I get a replacement key?\n\nThanks,\nDanielle\nUnit 5"},
        {"from_name": "Gregory Morgan", "from_email": "g.morgan.tenant@gmail.com", "subject": "Rent payment - Unit B1, 7 Ash Place", "body": "Hi,\n\nRent transferred this morning. Please confirm.\n\nGregory Morgan\nUnit B1"},
        {"from_name": "AllPro Maintenance", "from_email": "allpro.maintenance@gmail.com", "subject": "Monthly maintenance report - January 2026", "body": "Hi,\n\nHere's the summary of maintenance work completed across your properties in January:\n\n- 14 work orders completed\n- 3 emergency calls\n- Average response time: 1.2 business days\n- 2 work orders pending (awaiting parts)\n\nDetailed report attached.\n\nAllPro Maintenance"},
        {"from_name": "AllPro Maintenance", "from_email": "allpro.maintenance@gmail.com", "subject": "Invoice - Monthly maintenance contract, January 2026", "body": "Hi,\n\nInvoice for January maintenance services:\n\nInvoice #APM-2026-01\nMonthly retainer (20 properties): $3,200.00\nEmergency call-outs (3x): $450.00\nTotal: $3,650.00\n\nPayment due within 30 days.\n\nAllPro Maintenance"},
        {"from_name": "Melissa Rogers", "from_email": "melissa.r.tenant@gmail.com", "subject": "Question about lease clause - Unit 7, 400 Willow Terrace", "body": "Hi,\n\nI have a quick question about my lease. Section 8 mentions a \"common area maintenance fee\" but I don't see it as a separate line item on my rent statement. Is it included in the base rent or is it billed separately?\n\nThanks,\nMelissa Rogers\nUnit 7"},
        {"from_name": "Tyler Green", "from_email": "tyler.green.apt@gmail.com", "subject": "Rent payment - Unit 3A, 12 Oak Street", "body": "Hi,\n\nRent sent for this month. Cheers.\n\nTyler\nUnit 3A"},
        {"from_name": "Barbara Harris", "from_email": "barbara.h.lease@gmail.com", "subject": "Move-in checklist question - Unit 4D, 45 Maple Avenue", "body": "Hi,\n\nI'm going through the move-in checklist and noticed a small chip in the kitchen countertop near the sink. I want to document it so I'm not charged for it when I move out. Should I email photos to you or fill out a form?\n\nThanks,\nBarbara Harris\nUnit 4D"},
        {"from_name": "Heather Campbell", "from_email": "h.campbell.lease@gmail.com", "subject": "Rent confirmation - Unit 2B, 55 Walnut Drive", "body": "Hi,\n\nThis month's rent has been sent. Please confirm.\n\nHeather Campbell\nUnit 2B"},
        {"from_name": "Rachel Collins", "from_email": "rachel.c.renter@gmail.com", "subject": "Question about storage units - 18 Spruce Way", "body": "Hi,\n\nAre there any storage units available in the basement of 18 Spruce Way? I have some seasonal items I'd like to store. If so, what's the monthly cost?\n\nThanks,\nRachel Collins\nUnit 202"},
        {"from_name": "Andrew Mitchell", "from_email": "andrew.m.tenant@gmail.com", "subject": "Rent payment - Unit 301, 103 Birch Court", "body": "Hi,\n\nRent transferred today.\n\nAndrew Mitchell\nUnit 301"},
        {"from_name": "Ashley Robinson", "from_email": "ashley.robinson.unit@gmail.com", "subject": "Intercom not working - Unit 202, 78 Pine Road", "body": "Hi,\n\nThe intercom/buzzer for my unit (202) at 78 Pine Road doesn't seem to be working. Visitors can't buzz up to me. Could someone take a look?\n\nThanks,\nAshley Robinson\nUnit 202"},
        {"from_name": "Matthew Martin", "from_email": "matt.martin.tenant@gmail.com", "subject": "Rent sent - Unit 101, 78 Pine Road", "body": "Hi,\n\nJust a heads up that rent was transferred this morning.\n\nMatt\nUnit 101"},
    ],
    "day1": [
        {"from_name": "Zachary Morris", "from_email": "z.morris.renter@gmail.com", "subject": "Rent payment - Unit 6, 400 Willow Terrace", "body": "Hi,\n\nRent sent this morning via e-transfer.\n\nZach\nUnit 6"},
        {"from_name": "Brittany Carter", "from_email": "b.carter.lease@gmail.com", "subject": "Question about guest policy - Unit 202, 103 Birch Court", "body": "Hi,\n\nMy boyfriend is staying with me for a few weeks while his apartment is being renovated. Do I need to notify you or add him to the lease temporarily?\n\nThanks,\nBrittany\nUnit 202"},
        {"from_name": "Justin Roberts", "from_email": "justin.r.renter@gmail.com", "subject": "Rent payment - Unit 1A, 55 Walnut Drive", "body": "Hi,\n\nRent transferred. Please confirm.\n\nJustin Roberts\nUnit 1A"},
        {"from_name": "Eric Parker", "from_email": "eric.parker.unit@gmail.com", "subject": "Hallway carpet stain - 18 Spruce Way", "body": "Hi,\n\nThere's a large coffee stain on the hallway carpet on the 1st floor of 18 Spruce Way. It's been there for a few days. Could the cleaning crew address it?\n\nThanks,\nEric Parker\nUnit 101"},
    ],
    "day2": [
        {"from_name": "Vanessa Rivera", "from_email": "v.rivera.tenant@gmail.com", "subject": "Rent payment - Unit 201, 92 Hawthorn Gardens", "body": "Hi,\n\nRent has been transferred for this month.\n\nVanessa Rivera\nUnit 201"},
        {"from_name": "Sean Murphy", "from_email": "sean.murphy.renter@gmail.com", "subject": "Laundry room hours question - 92 Hawthorn Gardens", "body": "Hi,\n\nQuick question \u2014 what are the official laundry room hours? I've been doing laundry late at night and want to make sure I'm not breaking any rules.\n\nThanks,\nSean\nUnit 101"},
    ],
    "day3": [
        {"from_name": "Monica Richardson", "from_email": "m.richardson.lease@gmail.com", "subject": "Thank you for the elevator repair", "body": "Dear Property Manager,\n\nI just wanted to say thank you for getting the elevator fixed. It makes such a difference for me. I know Mr. Cooper can be difficult but please know that most of us appreciate your efforts.\n\nWarm regards,\nMonica Richardson\nUnit 401"},
        {"from_name": "Barbara Harris", "from_email": "barbara.h.lease@gmail.com", "subject": "Rent payment - Unit 4D, 45 Maple Avenue", "body": "Hi,\n\nRent sent today.\n\nBarbara\nUnit 4D"},
    ],
    "day4": [
        {"from_name": "David Chen", "from_email": "david.chen.renter@gmail.com", "subject": "Rent payment - 203 Elm Street", "body": "Hi,\n\nRent transferred this morning.\n\nDavid Chen"},
        {"from_name": "Michael Brown", "from_email": "mbrown.tenant@gmail.com", "subject": "Rent payment - 156 Magnolia Court", "body": "Hi,\n\nRent sent.\n\nMichael Brown"},
    ],
    "month1": [
        {"from_name": "GreenLeaf Landscaping", "from_email": "greenleaf.quotes@gmail.com", "subject": "Quarterly landscaping service - spring schedule", "body": "Hi,\n\nSpring is coming up and we'd like to confirm the quarterly landscaping schedule for your properties. Same properties as last quarter. We'll also be adding spring flower planting this time.\n\nUpdated quarterly rate: $1,350.00 (includes spring planting)\n\nPlease confirm.\n\nGreenLeaf Landscaping"},
        {"from_name": "AllPro Maintenance", "from_email": "allpro.maintenance@gmail.com", "subject": "Monthly maintenance report - February 2026", "body": "Hi,\n\nFebruary maintenance summary:\n\n- 18 work orders completed\n- 5 emergency calls (elevator, pipe burst, etc.)\n- Average response time: 0.8 business days\n- 1 work order pending\n\nNotable: Higher than usual emergency calls this month. Recommend preventive inspections on older plumbing and elevator systems.\n\nAllPro Maintenance"},
        {"from_name": "AllPro Maintenance", "from_email": "allpro.maintenance@gmail.com", "subject": "Invoice - Monthly maintenance contract, February 2026", "body": "Hi,\n\nInvoice for February maintenance services:\n\nInvoice #APM-2026-02\nMonthly retainer: $3,200.00\nEmergency call-outs (5x): $750.00\nTotal: $3,950.00\n\nPayment due within 30 days.\n\nAllPro Maintenance"},
        {"from_name": "Linda Taylor", "from_email": "linda.taylor.apt@gmail.com", "subject": "Rent payment - 8 Whispering Pines Road", "body": "Hi,\n\nRent sent for this month.\n\nLinda Taylor"},
        {"from_name": "Zachary Morris", "from_email": "z.morris.renter@gmail.com", "subject": "Rent payment - Unit 6, 400 Willow Terrace", "body": "Hi,\n\nRent transferred.\n\nZach"},
    ],
    "month2": [
        {"from_name": "BrightStar Cleaning Co.", "from_email": "brightstar.cleaning@gmail.com", "subject": "Cleaning schedule update - April 2026", "body": "Hi,\n\nJust a heads up that we'll be doing a deep clean of all common areas during the first week of April. This includes carpet shampooing in lobbies and stairwells.\n\nNo change in pricing. Please notify tenants about potential wet floors.\n\nBrightStar Cleaning Co."},
        {"from_name": "Redline Fire Safety", "from_email": "redline.firesafety@gmail.com", "subject": "Fire extinguisher inspection reminder", "body": "Hi,\n\nThis is a reminder that fire extinguisher inspections are due next month for all your multi-unit properties. We can schedule all buildings in one week.\n\nPlease confirm dates that work.\n\nRedline Fire Safety"},
        {"from_name": "Jessica Martinez", "from_email": "jessica.m.renter@gmail.com", "subject": "Rent payment - 19 Foxglove Way", "body": "Hi,\n\nRent sent.\n\nJessica"},
        {"from_name": "Brian Walker", "from_email": "brian.w.apt@gmail.com", "subject": "Rent payment - Unit 1, 231 Elm Blvd", "body": "Hi,\n\nRent transferred today.\n\nBrian"},
    ],
}

# ===================================================================
# SPAM EMAILS — generic business solicitations
# ===================================================================
SPAM_EMAILS = {
    "history": [
        {"from_name": "OfficeMax Pro", "from_email": "deals@officemax-promo.com", "subject": "HUGE savings on office supplies - up to 40% off!", "body": "Don't miss our biggest sale of the year! Stock up on printer paper, toner, pens, and more.\n\nUse code SAVE40 at checkout.\n\nFree shipping on orders over $50.\n\nOfficeMax Pro\nUnsubscribe: reply STOP"},
        {"from_name": "PropertyPro Software", "from_email": "sales@propertypro-demo.com", "subject": "Struggling with property management? Try PropertyPro FREE for 30 days", "body": "Hi Property Manager,\n\nTired of juggling spreadsheets and emails? PropertyPro streamlines rent collection, maintenance requests, and tenant communications in one platform.\n\nStart your free trial today \u2014 no credit card required.\n\nPropertyPro Software"},
        {"from_name": "National Landlord Insurance", "from_email": "quotes@nli-coverage.com", "subject": "Are you overpaying for landlord insurance? Get a free quote", "body": "Property owners save an average of $340/year when they switch to National Landlord Insurance.\n\nGet your free, no-obligation quote in 2 minutes.\n\nNational Landlord Insurance\n1-800-555-INSURE"},
        {"from_name": "CleanPro Supplies", "from_email": "orders@cleanpro-bulk.com", "subject": "Bulk cleaning supplies for property managers - FREE delivery", "body": "Stock up on cleaning supplies for your properties!\n\n- Floor cleaner (5 gal): $24.99\n- Trash bags (500 ct): $34.99\n- Disinfectant spray (case of 12): $29.99\n\nFree delivery on orders over $100.\n\nCleanPro Supplies"},
        {"from_name": "TaxHelper Pro", "from_email": "info@taxhelper-pro.com", "subject": "Maximize your rental property tax deductions this year", "body": "Are you claiming all the deductions you're entitled to? Most landlords miss at least 3 major deductions.\n\nDownload our free guide: \"Top 10 Tax Deductions Every Landlord Should Know\"\n\nTaxHelper Pro"},
    ],
    "day1": [
        {"from_name": "SecureIT Solutions", "from_email": "sales@secureit-cameras.com", "subject": "Security cameras for apartment buildings - 50% off installation", "body": "Protect your properties with HD security cameras. Our systems include:\n\n- 24/7 cloud recording\n- Motion detection alerts\n- Night vision\n- Mobile app access\n\n50% off installation this month only.\n\nSecureIT Solutions"},
    ],
    "day2": [
        {"from_name": "RentCollect Plus", "from_email": "demo@rentcollect-plus.com", "subject": "Automate your rent collection - zero late payments", "body": "Hi,\n\nRentCollect Plus automates rent collection with ACH direct debit. Tenants set it up once and you never chase a late payment again.\n\nSchedule a demo today.\n\nRentCollect Plus"},
    ],
    "day3": [],
    "day4": [
        {"from_name": "PrintFast Business Cards", "from_email": "orders@printfast-cards.com", "subject": "500 business cards for just $19.99!", "body": "Make a great first impression! Premium business cards starting at $19.99 for 500.\n\nFree design templates available.\n\nPrintFast Business Cards"},
    ],
    "month1": [
        {"from_name": "LandlordLegal.com", "from_email": "info@landlordlegal-help.com", "subject": "Free eviction notice templates - download now", "body": "Need to serve an eviction notice? Download our state-specific templates for free.\n\nWe also offer flat-rate legal consultations for landlords starting at $99.\n\nLandlordLegal.com"},
    ],
    "month2": [
        {"from_name": "EcoSmart Energy", "from_email": "savings@ecosmart-audit.com", "subject": "Cut your property energy bills by 30% - free energy audit", "body": "We help property managers reduce energy costs with LED upgrades, smart thermostats, and insulation improvements.\n\nSchedule your free energy audit today.\n\nEcoSmart Energy"},
    ],
}

# ===================================================================
# TIME-WASTER EMAILS — trivial tenant complaints/ramblings
# ===================================================================
TIMEWASTER_EMAILS = {
    "history": [
        {"from_name": "Crystal Bell", "from_email": "crystal.bell.apt@gmail.com", "subject": "Cat outside the building - 7 Ash Place", "body": "Hi,\n\nI've noticed a stray cat hanging around the entrance of 7 Ash Place for the past few days. It's an orange tabby and it looks friendly but I'm not sure if it belongs to anyone in the building. It meowed at me this morning for about 5 minutes straight.\n\nShould we do something about it? I'd take it in but my lease says no pets. Although I guess it's technically not MY pet if it just wanders in, right? Haha.\n\nAnyway, just thought you should know.\n\nCrystal\nUnit B2"},
        {"from_name": "Danielle Sanchez", "from_email": "d.sanchez.apt@gmail.com", "subject": "Hallway paint color - 400 Willow Terrace", "body": "Hi,\n\nI know this isn't urgent at all but I've been meaning to mention \u2014 the hallway paint color on our floor is really depressing. It's this grayish beige that makes the whole floor feel dark and institutional.\n\nHave you ever considered repainting? Even a warm white would make such a difference. I used to work in interior design (well, I took a class) and I think a soft cream or even a light sage green would really brighten things up.\n\nJust a thought!\n\nDanielle\nUnit 5"},
    ],
    "day1": [
        {"from_name": "Melissa Rogers", "from_email": "melissa.r.tenant@gmail.com", "subject": "Bird on my balcony - Unit 7, 400 Willow Terrace", "body": "Hi,\n\nThere's a pigeon that has been sitting on my balcony railing every single morning for the past week. It just sits there and stares at me through the glass door while I eat breakfast. It's honestly a little creepy.\n\nIs there anything the building can do? Like put up those spike things? I don't want to hurt it but I also don't want a pigeon watching me eat cereal every morning.\n\nThanks,\nMelissa\nUnit 7"},
    ],
    "day2": [
        {"from_name": "Crystal Bell", "from_email": "crystal.bell.apt@gmail.com", "subject": "Re: Cat outside the building - 7 Ash Place", "body": "Hi again,\n\nUpdate on the cat situation \u2014 the orange tabby is still here. I've been leaving a little bowl of water out for it (I hope that's okay). My neighbor Gregory says he's seen it too. We've named it Marmalade.\n\nI asked around and nobody in the building claims it. Should I call animal control? I feel bad doing that though. Marmalade seems happy here.\n\nLet me know what you think.\n\nCrystal\nUnit B2"},
    ],
    "day3": [],
    "day4": [
        {"from_name": "Danielle Sanchez", "from_email": "d.sanchez.apt@gmail.com", "subject": "Lobby music suggestion - 400 Willow Terrace", "body": "Hi,\n\nI was at a hotel last weekend and they had this lovely jazz music playing softly in the lobby. It made the whole place feel so upscale and welcoming.\n\nHave you ever thought about adding background music to the lobby at 400 Willow Terrace? I think it would really elevate the resident experience. I can send you a Spotify playlist if you want.\n\nJust an idea!\n\nDanielle\nUnit 5"},
    ],
    "month1": [
        {"from_name": "Crystal Bell", "from_email": "crystal.bell.apt@gmail.com", "subject": "Marmalade update - 7 Ash Place", "body": "Hi,\n\nJust wanted to let you know that the stray cat (Marmalade) has been adopted by a family down the street! They saw me feeding it and asked about it. They have a big yard and two kids who are thrilled.\n\nHappy ending for everyone. Thanks for not making a big deal about the water bowl.\n\nCrystal\nUnit B2"},
    ],
    "month2": [
        {"from_name": "Melissa Rogers", "from_email": "melissa.r.tenant@gmail.com", "subject": "The pigeon is back - Unit 7, 400 Willow Terrace", "body": "Hi,\n\nRemember the pigeon? It's back. Or maybe it's a different pigeon. Hard to tell. This one seems bolder though \u2014 it actually pecked at my sliding door this morning.\n\nI bought one of those plastic owl decoys from Amazon. Do you mind if I put it on the balcony railing? It's not permanent, just sits there.\n\nThanks,\nMelissa"},
    ],
}


# ===================================================================
# Programmatic filler — generates realistic routine emails to hit
# target counts per batch. Uses deterministic seeding so output is
# stable across runs.
# ===================================================================
import random as _random

_FILLER_TENANT_POOL = [
    ("James Smith", "james.smith.tenant@gmail.com", "14 Birchwood Lane", None),
    ("Maria Garcia", "maria.garcia.apt4b@gmail.com", "88 Sunset Drive", None),
    ("David Chen", "david.chen.renter@gmail.com", "203 Elm Street", None),
    ("Sarah Johnson", "sarah.j.tenant@gmail.com", "31 Harbor View Road", None),
    ("Michael Brown", "mbrown.tenant@gmail.com", "156 Magnolia Court", None),
    ("Robert Wilson", "rwilson.apt@gmail.com", "445 Lakeshore Blvd", None),
    ("Jessica Martinez", "jessica.m.renter@gmail.com", "19 Foxglove Way", None),
    ("William Anderson", "william.a.tenant@gmail.com", "267 Coventry Circle", None),
    ("Linda Taylor", "linda.taylor.apt@gmail.com", "8 Whispering Pines Road", None),
    ("Christopher Thomas", "c.thomas.renter@gmail.com", "45 Maple Avenue", "1A"),
    ("Patricia Jackson", "p.jackson.tenant@gmail.com", "45 Maple Avenue", "2B"),
    ("Barbara Harris", "barbara.h.lease@gmail.com", "45 Maple Avenue", "4D"),
    ("Matthew Martin", "matt.martin.tenant@gmail.com", "78 Pine Road", "101"),
    ("Ashley Robinson", "ashley.robinson.unit@gmail.com", "78 Pine Road", "202"),
    ("Stephanie Hall", "s.hall.tenant@gmail.com", "78 Pine Road", "404"),
    ("Brian Walker", "brian.w.apt@gmail.com", "231 Elm Blvd", "1"),
    ("Amanda Allen", "a.allen.lease@gmail.com", "231 Elm Blvd", "2"),
    ("Nicole King", "nicole.king.apt@gmail.com", "231 Elm Blvd", "4"),
    ("Joshua Wright", "j.wright.renter@gmail.com", "12 Oak Street", "2A"),
    ("Megan Scott", "megan.scott.unit@gmail.com", "12 Oak Street", "2B"),
    ("Tyler Green", "tyler.green.apt@gmail.com", "12 Oak Street", "3A"),
    ("Brittany Carter", "b.carter.lease@gmail.com", "103 Birch Court", "202"),
    ("Andrew Mitchell", "andrew.m.tenant@gmail.com", "103 Birch Court", "301"),
    ("Samantha Perez", "s.perez.apt@gmail.com", "103 Birch Court", "302"),
    ("Justin Roberts", "justin.r.renter@gmail.com", "55 Walnut Drive", "1A"),
    ("Heather Campbell", "h.campbell.lease@gmail.com", "55 Walnut Drive", "2B"),
    ("Eric Parker", "eric.parker.unit@gmail.com", "18 Spruce Way", "101"),
    ("Amber Evans", "amber.evans.tenant@gmail.com", "18 Spruce Way", "102"),
    ("Rachel Collins", "rachel.c.renter@gmail.com", "18 Spruce Way", "202"),
    ("Aaron Stewart", "aaron.s.tenant@gmail.com", "400 Willow Terrace", "4"),
    ("Danielle Sanchez", "d.sanchez.apt@gmail.com", "400 Willow Terrace", "5"),
    ("Zachary Morris", "z.morris.renter@gmail.com", "400 Willow Terrace", "6"),
    ("Melissa Rogers", "melissa.r.tenant@gmail.com", "400 Willow Terrace", "7"),
    ("Patrick Reed", "p.reed.apt@gmail.com", "7 Ash Place", "A1"),
    ("Tiffany Cook", "tiffany.cook.lease@gmail.com", "7 Ash Place", "A2"),
    ("Gregory Morgan", "g.morgan.tenant@gmail.com", "7 Ash Place", "B1"),
    ("Crystal Bell", "crystal.bell.apt@gmail.com", "7 Ash Place", "B2"),
    ("Sean Murphy", "sean.murphy.renter@gmail.com", "92 Hawthorn Gardens", "101"),
    ("Vanessa Rivera", "v.rivera.tenant@gmail.com", "92 Hawthorn Gardens", "201"),
    ("Monica Richardson", "m.richardson.lease@gmail.com", "92 Hawthorn Gardens", "401"),
]

_RENT_SUBJECTS = [
    "Rent payment sent - {addr}",
    "Rent for this month - {addr}",
    "Monthly rent transferred - {addr}",
    "Rent confirmation - {addr}",
    "Rent deposited - {addr}",
]
_RENT_BODIES = [
    "Hi,\n\nJust confirming rent was sent via e-transfer this morning.\n\nThanks,\n{name}",
    "Hi,\n\nRent for this month has been transferred. Please confirm receipt.\n\n{name}",
    "Hi,\n\nMonthly rent deposited today.\n\nThanks,\n{name}\n{addr}",
    "Hi,\n\nRent sent. Let me know if there are any issues.\n\n{name}",
    "Hi,\n\nJust a heads up that rent was transferred this morning.\n\nCheers,\n{name}",
]

_MAINT_SUBJECTS = [
    "Minor repair needed - {addr}",
    "Small maintenance request - {addr}",
    "Quick fix needed - {addr}",
    "Maintenance question - {addr}",
]
_MAINT_BODIES = [
    "Hi,\n\nThe bathroom door handle is loose in my unit at {addr}. It still works but it wobbles. Could maintenance tighten it when they're in the building?\n\nThanks,\n{name}",
    "Hi,\n\nOne of the kitchen cabinet doors at {addr} has a loose hinge. It doesn't close properly. Not urgent but would be nice to get fixed.\n\nThanks,\n{name}",
    "Hi,\n\nThe weather stripping on my front door at {addr} is peeling. I can feel a draft coming in. Could someone replace it?\n\n{name}",
    "Hi,\n\nThe towel rack in my bathroom at {addr} came off the wall. I think the drywall anchors gave out. Could maintenance reinstall it with proper anchors?\n\nThanks,\n{name}",
    "Hi,\n\nThe kitchen faucet at {addr} has started dripping slightly. It's not bad yet but I wanted to report it before it gets worse.\n\n{name}",
    "Hi,\n\nThe screen door at {addr} has a small tear in the mesh. Bugs are getting in. Could you have it patched or replaced?\n\nThanks,\n{name}",
    "Hi,\n\nThe closet light in the master bedroom at {addr} burned out. It's one of those fixtures I can't reach. Could maintenance swap the bulb?\n\n{name}",
    "Hi,\n\nThe toilet in my unit at {addr} runs intermittently. It stops on its own but wastes water. Probably needs a new flapper valve.\n\nThanks,\n{name}",
]

_QUESTION_SUBJECTS = [
    "Quick question - {addr}",
    "Question about building policy - {addr}",
    "Lease question - {addr}",
    "General inquiry - {addr}",
]
_QUESTION_BODIES = [
    "Hi,\n\nAm I allowed to install a Ring doorbell camera at my unit ({addr})? I want to make sure it's okay before I drill any holes.\n\nThanks,\n{name}",
    "Hi,\n\nIs there a recycling bin for the building at {addr}? I've been putting everything in the regular trash but I'd prefer to recycle.\n\n{name}",
    "Hi,\n\nWhat's the policy on hanging things on the walls at {addr}? I want to put up some shelves but don't want to lose my deposit.\n\nThanks,\n{name}",
    "Hi,\n\nDo you have a recommended locksmith? I'd like to get a spare key made for my unit at {addr}.\n\n{name}",
    "Hi,\n\nIs there a BBQ grill available for residents at {addr}? I saw a patio area but wasn't sure if grilling is allowed.\n\nThanks,\n{name}",
    "Hi,\n\nQuick question \u2014 when is trash pickup day for {addr}? I just moved in and want to make sure I put the bins out on the right day.\n\n{name}",
    "Hi,\n\nCan I paint the walls in my unit at {addr}? I'd repaint them back to the original color before moving out.\n\nThanks,\n{name}",
    "Hi,\n\nIs there a community bulletin board at {addr}? I'd like to post a note about a lost set of keys.\n\n{name}",
]

_MONTHS = ["October", "November", "December", "January"]


def _generate_filler(batch: str, target: int, current: int) -> list:
    """Generate filler emails to reach target count for a batch."""
    needed = max(0, target - current)
    if needed == 0:
        return []

    rng = _random.Random(f"elron-filler-{batch}")
    filler = []

    for i in range(needed):
        tenant = rng.choice(_FILLER_TENANT_POOL)
        name, email, address, unit = tenant
        addr = f"Unit {unit}, {address}" if unit else address
        fmt = {"name": name, "addr": addr}

        roll = rng.random()
        if roll < 0.50:
            subj = rng.choice(_RENT_SUBJECTS).format(**fmt)
            body = rng.choice(_RENT_BODIES).format(**fmt)
        elif roll < 0.80:
            subj = rng.choice(_MAINT_SUBJECTS).format(**fmt)
            body = rng.choice(_MAINT_BODIES).format(**fmt)
        else:
            subj = rng.choice(_QUESTION_SUBJECTS).format(**fmt)
            body = rng.choice(_QUESTION_BODIES).format(**fmt)

        # Add month variation for history
        if batch == "history":
            month = rng.choice(_MONTHS)
            subj = subj.replace("this month", month).replace("Rent for", f"Rent for {month} -")

        filler.append({
            "from_name": name,
            "from_email": email,
            "subject": subj,
            "body": body,
        })

    return filler


# Target email counts per batch
_BATCH_TARGETS = {
    "history": 300,
    "day1": 50,
    "day2": 40,
    "day3": 35,
    "day4": 30,
    "month1": 40,
    "month2": 35,
}


# ===================================================================
# Helper: collect all emails for a given batch
# ===================================================================
def get_emails_for_batch(batch: str) -> list:
    """Return a flat list of all email dicts for the given batch."""
    emails = []
    for storyline in STORYLINES:
        for email in storyline["emails"]:
            if email["batch"] == batch:
                emails.append({
                    **email,
                    "storyline_id": storyline["id"],
                    "thread_subject": storyline["thread_subject"],
                })
    for email in ROUTINE_EMAILS.get(batch, []):
        emails.append({**email, "batch": batch, "storyline_id": None, "thread_subject": None, "is_reply": False})
    for email in SPAM_EMAILS.get(batch, []):
        emails.append({**email, "batch": batch, "storyline_id": None, "thread_subject": None, "is_reply": False})
    for email in TIMEWASTER_EMAILS.get(batch, []):
        emails.append({**email, "batch": batch, "storyline_id": None, "thread_subject": None, "is_reply": False})

    # Pad with generated filler to hit target counts
    target = _BATCH_TARGETS.get(batch, 0)
    if len(emails) < target:
        for filler_email in _generate_filler(batch, target, len(emails)):
            emails.append({**filler_email, "batch": batch, "storyline_id": None, "thread_subject": None, "is_reply": False})

    return emails
