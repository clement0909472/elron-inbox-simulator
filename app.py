import base64
import email.mime.text
import json
import os
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, jsonify, render_template_string

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = Flask(__name__)

SCOPES = ["https://mail.google.com/"]
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"
TARGET_EMAIL = "relaylegacy@gmail.com"

# ---------------------------------------------------------------------------
# Gmail auth
# ---------------------------------------------------------------------------

def get_gmail_service():
    creds = None

    # Production (Vercel): load from environment variables
    token_env = os.environ.get("GOOGLE_TOKEN")
    creds_env = os.environ.get("GOOGLE_CREDENTIALS")

    if token_env:
        creds = Credentials.from_authorized_user_info(json.loads(token_env), SCOPES)
    elif os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        elif creds_env:
            # On Vercel with no valid token — token env var needs updating
            raise Exception("Token missing or expired. Re-run auth locally and update the GOOGLE_TOKEN env var on Vercel.")
        else:
            # Local dev: open browser flow
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
            with open(TOKEN_FILE, "w") as token:
                token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


# ---------------------------------------------------------------------------
# Email generation  — 1000+ unique combinations
# ---------------------------------------------------------------------------

TENANTS = [
    ("James Smith", "james.smith.tenant@gmail.com"),
    ("Maria Garcia", "maria.garcia.apt4b@gmail.com"),
    ("David Chen", "david.chen.renter@gmail.com"),
    ("Sarah Johnson", "sarah.j.tenant@gmail.com"),
    ("Michael Brown", "mbrown.tenant@gmail.com"),
    ("Emily Davis", "emily.davis.lease@gmail.com"),
    ("Robert Wilson", "rwilson.apt@gmail.com"),
    ("Jessica Martinez", "jessica.m.renter@gmail.com"),
    ("William Anderson", "william.a.tenant@gmail.com"),
    ("Linda Taylor", "linda.taylor.apt@gmail.com"),
    ("Christopher Thomas", "c.thomas.renter@gmail.com"),
    ("Patricia Jackson", "p.jackson.tenant@gmail.com"),
    ("Daniel White", "d.white.apt12@gmail.com"),
    ("Barbara Harris", "barbara.h.lease@gmail.com"),
    ("Matthew Martin", "matt.martin.tenant@gmail.com"),
    ("Ashley Robinson", "ashley.robinson.unit@gmail.com"),
    ("Kevin Lee", "kevin.lee.renter@gmail.com"),
    ("Stephanie Hall", "s.hall.tenant@gmail.com"),
    ("Brian Walker", "brian.w.apt@gmail.com"),
    ("Amanda Allen", "a.allen.lease@gmail.com"),
    ("Ryan Young", "ryan.young.tenant@gmail.com"),
    ("Nicole King", "nicole.king.apt@gmail.com"),
    ("Joshua Wright", "j.wright.renter@gmail.com"),
    ("Megan Scott", "megan.scott.unit@gmail.com"),
    ("Tyler Green", "tyler.green.apt@gmail.com"),
    ("Kayla Adams", "kayla.adams.tenant@gmail.com"),
    ("Nathan Baker", "n.baker.renter@gmail.com"),
    ("Brittany Carter", "b.carter.lease@gmail.com"),
    ("Andrew Mitchell", "andrew.m.tenant@gmail.com"),
    ("Samantha Perez", "s.perez.apt@gmail.com"),
    ("Justin Roberts", "justin.r.renter@gmail.com"),
    ("Lauren Turner", "l.turner.tenant@gmail.com"),
    ("Brandon Phillips", "b.phillips.apt@gmail.com"),
    ("Heather Campbell", "h.campbell.lease@gmail.com"),
    ("Eric Parker", "eric.parker.unit@gmail.com"),
    ("Amber Evans", "amber.evans.tenant@gmail.com"),
    ("Jonathan Edwards", "jon.edwards.apt@gmail.com"),
    ("Rachel Collins", "rachel.c.renter@gmail.com"),
    ("Aaron Stewart", "aaron.s.tenant@gmail.com"),
    ("Danielle Sanchez", "d.sanchez.apt@gmail.com"),
    ("Zachary Morris", "z.morris.renter@gmail.com"),
    ("Melissa Rogers", "melissa.r.tenant@gmail.com"),
    ("Patrick Reed", "p.reed.apt@gmail.com"),
    ("Tiffany Cook", "tiffany.cook.lease@gmail.com"),
    ("Gregory Morgan", "g.morgan.tenant@gmail.com"),
    ("Crystal Bell", "crystal.bell.apt@gmail.com"),
    ("Sean Murphy", "sean.murphy.renter@gmail.com"),
    ("Vanessa Rivera", "v.rivera.tenant@gmail.com"),
    ("Derek Cooper", "derek.cooper.apt@gmail.com"),
    ("Monica Richardson", "m.richardson.lease@gmail.com"),
]

CONTRACTORS = [
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
]

EMAIL_TEMPLATES = [
    # --- Leaky faucet / plumbing ---
    {
        "subject_templates": [
            "Leaking faucet in unit {unit} - urgent",
            "Water dripping from kitchen tap - Unit {unit}",
            "Bathroom faucet won't stop dripping - {unit}",
            "Faucet leak getting worse, need repair ASAP",
            "Kitchen sink dripping constantly - Unit {unit}",
            "Plumbing issue in my unit - faucet",
            "Please fix leaking tap in {unit}",
        ],
        "body_templates": [
            (
                "Hi,\n\nI'm reaching out about a leaking faucet in my kitchen (Unit {unit}). "
                "It's been dripping constantly for {days} days now and my water bill is going up. "
                "Could you please send someone to fix it this week?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nThe bathroom faucet in Unit {unit} has started leaking pretty badly. "
                "There's water pooling under the sink cabinet. I've put a bucket down but I really "
                "need maintenance to look at it.\n\nBest,\n{name}"
            ),
            (
                "Hi there,\n\nThe kitchen faucet in my unit ({unit}) has been leaking for {days} days. "
                "I've tried tightening it myself but it's getting worse. The dripping is also keeping "
                "me up at night. Can someone come by this week?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nJust a heads up — there's a slow drip under the bathroom sink in Unit {unit}. "
                "I noticed a small puddle this morning. It doesn't seem urgent yet but I'd rather get "
                "it looked at before it causes damage.\n\nThanks,\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Late rent ---
    {
        "subject_templates": [
            "Rent payment for {month} - delay notice",
            "Late rent - Unit {unit}",
            "Regarding this month's rent",
            "Payment coming {days} days late - heads up",
            "Late payment notification - {month}",
            "Heads up: rent will be late this month",
            "Delayed rent for {month} - Unit {unit}",
        ],
        "body_templates": [
            (
                "Hi,\n\nI wanted to let you know that my rent for {month} will be {days} days late. "
                "I had an unexpected expense come up but I will have it paid in full by {date}. "
                "I apologize for any inconvenience.\n\nRegards,\n{name}"
            ),
            (
                "Hello,\n\nUnfortunately my paycheck from work was delayed this week. "
                "I won't be able to pay rent for Unit {unit} until {date}. "
                "I can pay a portion now if that helps. Please let me know.\n\n{name}"
            ),
            (
                "Hi,\n\nI'm writing to let you know my {month} rent will be about {days} days late. "
                "I had a medical bill come up unexpectedly. I will transfer the full amount by {date} "
                "and can provide documentation if needed.\n\nSorry for the trouble,\n{name}"
            ),
            (
                "Hello,\n\nI just wanted to give you advance notice that my rent payment for this month "
                "will be delayed. My employer switched payroll systems and direct deposit is running "
                "{days} days behind. Full payment will be made by {date}.\n\nThank you for understanding,\n{name}"
            ),
            (
                "Hi,\n\nQuick note — I'll be {days} days late on rent this month for Unit {unit}. "
                "Lost my part-time job last week and am sorting things out. I will definitely have it "
                "by {date} and will let you know if anything changes.\n\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Lease renewal ---
    {
        "subject_templates": [
            "Lease renewal inquiry - Unit {unit}",
            "Renewing my lease - questions",
            "Lease ending {month} - renewal options?",
            "Interested in renewing for another year",
            "My lease is up in {month} - what are next steps?",
            "Renewal paperwork for Unit {unit}",
            "Staying another year - lease renewal request",
        ],
        "body_templates": [
            (
                "Hi,\n\nMy current lease for Unit {unit} is up at the end of {month}. "
                "I'd love to stay another year. Could you send me the renewal paperwork and let me "
                "know if there will be any rent increase?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nI received the notice that my lease expires {month} {year}. "
                "I'm very happy here and would like to renew. What's the process? "
                "Is the rent going up?\n\nBest regards,\n{name}"
            ),
            (
                "Hi,\n\nI've been in Unit {unit} for a year now and I'd like to stay. "
                "My lease ends in {month} — could we discuss renewal terms? "
                "I'm hoping to lock in a 12-month lease again.\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nWould it be possible to do a month-to-month arrangement after my lease "
                "in Unit {unit} ends in {month}? I may be relocating for work in {year} and want "
                "some flexibility. Happy to discuss.\n\n{name}"
            ),
            (
                "Hi,\n\nLease renewal question — I'm in Unit {unit} and my lease ends {month} {year}. "
                "If I renew for two years instead of one, is there any discount on rent? "
                "I love the apartment and want to commit long-term.\n\nThanks,\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Noise complaint ---
    {
        "subject_templates": [
            "Noise complaint - unit above me",
            "Ongoing noise issue - please help",
            "Loud neighbors in Unit {unit} again",
            "Noise disturbance - {time} last night",
            "Repeated noise problem from upstairs",
            "Noise complaint for Unit {unit}",
            "Neighbor disturbance keeping me up",
            "Can you speak to the tenant in Unit {unit}?",
        ],
        "body_templates": [
            (
                "Hi,\n\nI'm writing to complain about excessive noise coming from the unit above mine "
                "(Unit {unit}). This has been going on for {days} days. Last night it went until {time}. "
                "Could you please speak with them?\n\nThank you,\n{name}"
            ),
            (
                "Hello,\n\nI hate to complain but the noise from Unit {unit} has been really disruptive. "
                "There's loud music and what sounds like furniture being dragged at all hours. "
                "I work early mornings and this is affecting my sleep. Please advise.\n\n{name}"
            ),
            (
                "Hi,\n\nThis is the third time I'm reaching out about the noise situation. "
                "The tenant above me (Unit {unit}) had a loud gathering again last night until {time}. "
                "I have work at 6 AM and this is becoming unbearable. "
                "Please take action.\n\nThank you,\n{name}"
            ),
            (
                "Hello,\n\nThere was a very loud party in Unit {unit} last night that went until {time}. "
                "Multiple neighbors were disturbed — I knocked on the door twice but got no response. "
                "Is there something in the lease about quiet hours?\n\n{name}"
            ),
            (
                "Hi,\n\nI've been patient but the noise from Unit {unit} is really affecting my quality "
                "of life. It's not just late nights — there's stomping and banging throughout the day too. "
                "This has been going on for {days} days straight.\n\nPlease help,\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Contractor quote ---
    {
        "subject_templates": [
            "Quote for {job} - {address}",
            "Estimate for {job} work at {address}",
            "Re: Service request - {job}",
            "{job} repair estimate enclosed",
            "Proposal for {job} at {address}",
            "Follow-up: {job} quote",
            "Revised estimate for {job}",
        ],
        "body_templates": [
            (
                "Hi,\n\nThank you for reaching out. Please find our estimate for {job} at {address} below.\n\n"
                "Labour: ${labour}\nMaterials: ${materials}\nTotal: ${total}\nEstimated time: {days} days\n\n"
                "We can start as early as next week. Please confirm at your convenience.\n\nBest,\n{name}\n{company}"
            ),
            (
                "Hello,\n\nFollowing our site visit on {date}, here is our formal quote for {job}:\n\n"
                "- Parts & materials: ${materials}\n- Labour ({hours} hrs @ $85/hr): ${labour}\n"
                "- Total: ${total}\n\nValid for 30 days. Let us know how you'd like to proceed.\n\n{name}\n{company}"
            ),
            (
                "Hi,\n\nAttached is our revised estimate for {job} at {address}. We were able to source "
                "materials at a lower cost than originally quoted.\n\n"
                "Updated total: ${total} (materials: ${materials}, labour: ${labour})\n\n"
                "We can mobilize within 3 business days of approval.\n\n{name}\n{company}"
            ),
            (
                "Hello,\n\nThis is a follow-up on our {job} quote for {address}. "
                "Our estimate of ${total} stands and our schedule has opened up — "
                "we could have a crew on-site by {date} if you'd like to move forward.\n\n"
                "Please let us know.\n\n{name}\n{company}"
            ),
        ],
        "sender_pool": "contractors",
    },
    # --- AC / heating not working ---
    {
        "subject_templates": [
            "AC not working in Unit {unit} - it's {temp}°F inside",
            "Heating broken in my apartment - urgent",
            "No heat in Unit {unit} since {days} days ago",
            "HVAC issue - Unit {unit} is overheating",
            "Air conditioning failed - Unit {unit}",
            "Thermostat broken in {unit}",
        ],
        "body_templates": [
            (
                "Hi,\n\nThe air conditioning in Unit {unit} stopped working {days} days ago. "
                "The temperature inside is {temp}°F and it's unbearable, especially at night. "
                "Could you please send maintenance as soon as possible?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nI have no heat in my unit ({unit}). It's been like this for {days} days "
                "and the temperature is dropping. I have a small child at home and this is a serious issue. "
                "Please treat this as urgent.\n\nThank you,\n{name}"
            ),
            (
                "Hi,\n\nThe HVAC system in Unit {unit} is blowing warm air regardless of the thermostat setting. "
                "I've reset the thermostat multiple times. It's {temp}°F inside right now. "
                "Can you send someone today?\n\n{name}"
            ),
            (
                "Hello,\n\nQuick heads up — the AC in {unit} has been making a loud grinding noise "
                "for {days} days and now it's stopped cooling entirely. I turned it off to avoid further "
                "damage. Please advise on when maintenance can come.\n\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Pest infestation ---
    {
        "subject_templates": [
            "Pest problem in Unit {unit} - needs attention",
            "Cockroach infestation - Unit {unit}",
            "Mice spotted in my apartment",
            "Pest control needed urgently - {unit}",
            "Roach sighting in Unit {unit} - please help",
            "Rodent issue in building - Unit {unit}",
        ],
        "body_templates": [
            (
                "Hi,\n\nI've been seeing cockroaches in my kitchen for the past {days} days (Unit {unit}). "
                "I've tried store-bought traps but they're not working. I believe the problem may be "
                "coming through shared walls. Can you schedule pest control?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nI spotted what looks like mouse droppings behind my stove in Unit {unit}. "
                "I haven't seen any mice yet but I'm very concerned. Could you have pest control "
                "come and inspect the unit as soon as possible?\n\n{name}"
            ),
            (
                "Hi,\n\nThis is the second time I've raised a pest issue in Unit {unit}. "
                "Despite the treatment {days} weeks ago, I'm still seeing roaches in the bathroom. "
                "Whatever was done doesn't seem to have worked. Please arrange a follow-up.\n\n{name}"
            ),
            (
                "Hello,\n\nI found a trail of ants coming in through the kitchen windowsill in Unit {unit}. "
                "It started small but there are now dozens of them every morning. "
                "Please send pest control at your earliest convenience.\n\nThanks,\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Water damage / flooding ---
    {
        "subject_templates": [
            "Water leak from upstairs - Unit {unit} flooding",
            "Ceiling leak in my apartment - urgent",
            "Water damage in Unit {unit} - needs immediate attention",
            "Pipe burst - water on the floor in {unit}",
            "Leaking ceiling - Unit {unit}",
        ],
        "body_templates": [
            (
                "Hi,\n\nThere is water leaking through my ceiling in Unit {unit} — it seems to be "
                "coming from the unit above. There's a large stain and active dripping. "
                "I've placed towels down but this is getting worse. Please send someone immediately.\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nEmergency — a pipe appears to have burst in my bathroom wall (Unit {unit}). "
                "Water is pooling on the floor and running into the hallway. "
                "I've turned off the water main. Please call me at your earliest convenience.\n\n{name}"
            ),
            (
                "Hi,\n\nThere's been a slow ceiling leak in my bedroom (Unit {unit}) for {days} days. "
                "It started as a small stain but now it's dripping when it rains. "
                "I'm worried about mold developing. Can you schedule an inspection?\n\n{name}"
            ),
            (
                "Hello,\n\nI came home to find water dripping from the kitchen light fixture in Unit {unit}. "
                "I've switched off the circuit breaker for safety. This is a potential electrical hazard. "
                "Please prioritize this.\n\nThank you,\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Broken appliance ---
    {
        "subject_templates": [
            "Dishwasher broken in Unit {unit}",
            "Oven not working - Unit {unit}",
            "Washer/dryer issue in my unit",
            "Refrigerator stopped cooling - Unit {unit}",
            "Garbage disposal broken - Unit {unit}",
            "Stove burner not working in {unit}",
        ],
        "body_templates": [
            (
                "Hi,\n\nThe dishwasher in Unit {unit} stopped working {days} days ago. "
                "It fills with water but won't drain. I've tried resetting it but no luck. "
                "Could maintenance take a look?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nThe refrigerator in my unit ({unit}) isn't keeping things cold. "
                "I noticed my food spoiling and the freezer isn't freezing either. "
                "I had to throw out quite a bit of groceries. Can you arrange a repair or replacement?\n\n{name}"
            ),
            (
                "Hi,\n\nTwo of the four burners on my stove aren't working in Unit {unit}. "
                "The oven still works but the front two burners have no ignition. "
                "This has been the case for {days} days. Please send someone to fix it.\n\n{name}"
            ),
            (
                "Hello,\n\nThe garbage disposal in Unit {unit} stopped working and is now making a "
                "humming noise when I flip the switch. I've tried the reset button at the bottom "
                "but it keeps tripping. Can maintenance come and take a look?\n\nThanks,\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Move-out notice ---
    {
        "subject_templates": [
            "Move-out notice - Unit {unit}",
            "Notice to vacate - {month}",
            "Giving {days}-day notice for Unit {unit}",
            "Ending my tenancy - Unit {unit}",
            "Vacating Unit {unit} at end of {month}",
            "30-day notice of move-out",
        ],
        "body_templates": [
            (
                "Hi,\n\nI am writing to give formal notice that I will be vacating Unit {unit} "
                "at the end of {month}. This serves as my {days}-day notice as required by my lease. "
                "Please let me know what I need to do regarding the move-out inspection and "
                "security deposit return.\n\nThank you,\n{name}"
            ),
            (
                "Hello,\n\nI wanted to give you advance notice that I'll be moving out of Unit {unit} "
                "by the end of {month}. I've truly enjoyed living here. "
                "Could you send me the move-out checklist so I can prepare the apartment properly?\n\nBest,\n{name}"
            ),
            (
                "Hi,\n\nPlease accept this as my official 30-day notice to vacate Unit {unit}. "
                "My last day will be {date}. I'll be available for the walk-through inspection "
                "on the final day or a day prior — whatever works best for you.\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nDue to a job relocation, I need to vacate Unit {unit} by {date}. "
                "I understand my lease runs through {month} and I'd like to discuss early termination "
                "options and any applicable fees.\n\nPlease let me know how to proceed.\n\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Parking complaint ---
    {
        "subject_templates": [
            "Someone in my parking spot again - Unit {unit}",
            "Parking issue - unauthorized vehicle",
            "Unassigned car blocking my spot",
            "Parking complaint - please help",
            "Car blocking Unit {unit} parking spot for {days} days",
        ],
        "body_templates": [
            (
                "Hi,\n\nFor the {days}th time this month, someone has parked in my assigned spot "
                "(Unit {unit}). I had to park on the street last night. Could you please send a notice "
                "to all residents or arrange for the vehicle to be towed?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nThere's an unfamiliar car that has been parked in my spot for {days} days. "
                "It has no visible permit. I've left a note on the windshield twice but it's still there. "
                "Can you help resolve this?\n\n{name}"
            ),
            (
                "Hi,\n\nI wanted to flag a parking issue. A vehicle has been double-parked in the lot "
                "blocking several spots including mine (Unit {unit}). This has been happening repeatedly "
                "in the evenings. Could you check if it belongs to a resident?\n\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Mold / air quality ---
    {
        "subject_templates": [
            "Mold growing in Unit {unit} bathroom",
            "Mold concern - please inspect",
            "Black mold spotted in {unit}",
            "Ventilation and mold issue - Unit {unit}",
            "Air quality concern in my apartment",
        ],
        "body_templates": [
            (
                "Hi,\n\nI've noticed black mold growing along the grout lines in my bathroom (Unit {unit}). "
                "The bathroom fan doesn't seem to be working properly which may be the cause. "
                "I'm concerned about health implications. Can you send someone to inspect?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nThere's a musty smell coming from the closet in my bedroom (Unit {unit}). "
                "I moved some boxes and noticed what looks like mold on the wall behind them. "
                "Please have maintenance take a look before it spreads.\n\n{name}"
            ),
            (
                "Hi,\n\nI've been having respiratory issues for the past {days} days and I think "
                "it might be related to mold in my unit ({unit}). The bathroom walls are damp and "
                "there are dark spots forming. Can we get an inspection scheduled?\n\nThank you,\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- Security / access issue ---
    {
        "subject_templates": [
            "Front door lock broken - Unit {unit}",
            "Security concern - building entrance not locking",
            "Lost key fob - Unit {unit}",
            "Mailbox lock broken",
            "Building security issue - please address",
        ],
        "body_templates": [
            (
                "Hi,\n\nThe deadbolt on my front door (Unit {unit}) isn't latching properly. "
                "I can lock it with the key but it doesn't catch when I just close the door. "
                "This is a security concern. Can maintenance fix or replace the lock?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nI noticed the main entrance door to the building has not been locking "
                "properly for {days} days. It can be pushed open without a key fob. "
                "This is a safety issue for all residents. Please have it fixed urgently.\n\n{name}"
            ),
            (
                "Hi,\n\nI've lost my key fob for building access and need a replacement for Unit {unit}. "
                "Could you let me know the process and whether there's a replacement fee? "
                "In the meantime, can someone let me in this evening?\n\n{name}"
            ),
            (
                "Hello,\n\nMy mailbox lock in the lobby is broken — I haven't been able to access "
                "my mail for {days} days. Can you arrange a repair or provide a temporary solution?\n\nThanks,\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
    # --- General maintenance request ---
    {
        "subject_templates": [
            "Maintenance request - Unit {unit}",
            "Several small repairs needed in {unit}",
            "Maintenance checklist - Unit {unit}",
            "Repair request for Unit {unit}",
            "Items needing attention in my unit",
        ],
        "body_templates": [
            (
                "Hi,\n\nI have a few small items in Unit {unit} that need attention:\n\n"
                "1. The bathroom door doesn't close all the way\n"
                "2. One of the kitchen cabinet hinges is loose\n"
                "3. The window screen in the bedroom has a tear\n\n"
                "None are urgent but I wanted to log them. When's a good time for maintenance "
                "to swing by?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nCould I schedule a maintenance visit for Unit {unit}? "
                "The toilet has been running intermittently, and the bathroom exhaust fan "
                "is very loud. I'm free most weekday mornings if that works.\n\n{name}"
            ),
            (
                "Hi,\n\nQuick maintenance request for Unit {unit}: the kitchen faucet handle "
                "is loose and wobbles when used, and one of the bedroom light fixtures flickers. "
                "Can someone come take a look this week?\n\nThanks,\n{name}"
            ),
            (
                "Hello,\n\nI wanted to submit a maintenance request. The caulking around the bathtub "
                "in Unit {unit} is peeling and there are small gaps forming. I'm worried about water "
                "seeping into the wall. Can you have someone re-caulk it?\n\nThanks,\n{name}"
            ),
        ],
        "sender_pool": "tenants",
    },
]

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
JOBS = [
    "roof repair", "HVAC servicing", "plumbing inspection",
    "electrical panel upgrade", "drywall repair", "window replacement",
    "parking lot resurfacing", "boiler maintenance", "gutter cleaning",
    "exterior painting", "concrete crack repair", "fire alarm testing",
    "elevator inspection", "landscaping overhaul", "waterproofing",
    "deck repair", "insulation upgrade", "sump pump installation",
]
ADDRESSES = [
    "12 Oak Street", "45 Maple Ave", "78 Pine Rd", "231 Elm Blvd", "9 Cedar Lane",
    "103 Birch Court", "55 Walnut Drive", "18 Spruce Way", "400 Willow Terrace", "7 Ash Place",
]
TIMES = ["midnight", "1:00 AM", "2:30 AM", "11:45 PM", "12:30 AM", "1:45 AM", "11:00 PM", "2:00 AM"]
TEMPS = [84, 87, 89, 91, 93, 95, 52, 49, 46, 43]


def _random_date(month_name: str) -> str:
    day = random.randint(10, 28)
    return f"{month_name} {day}, 2026"


def generate_email(index: int) -> dict:
    template = random.choice(EMAIL_TEMPLATES)
    month = random.choice(MONTHS)
    unit = f"{random.randint(1, 12)}{random.choice(['A', 'B', 'C', 'D', 'E'])}"
    days = random.randint(2, 21)
    hours = random.randint(3, 14)
    materials = random.randint(80, 1200)
    labour = hours * 85
    total = materials + labour
    job = random.choice(JOBS)
    address = random.choice(ADDRESSES)
    temp = random.choice(TEMPS)

    if template["sender_pool"] == "contractors":
        company, sender_email = random.choice(CONTRACTORS)
        name = company.split("'")[0].split(" ")[0] + " (Estimator)"
        subject = random.choice(template["subject_templates"]).format(
            job=job, address=address
        )
        body = random.choice(template["body_templates"]).format(
            job=job, address=address, name=name, company=company,
            materials=materials, labour=labour, total=total,
            days=days, hours=hours, date=_random_date(month)
        )
    else:
        name, sender_email = random.choice(TENANTS)
        subject = random.choice(template["subject_templates"]).format(
            unit=unit, month=month, days=days, time=random.choice(TIMES), temp=temp
        )
        body = random.choice(template["body_templates"]).format(
            unit=unit, month=month, name=name.split()[0], days=days,
            date=_random_date(month), time=random.choice(TIMES), year=2026, temp=temp
        )

    return {"from_name": name, "from_email": sender_email, "subject": subject, "body": body}


def build_raw_message(from_name: str, from_email: str, subject: str, body: str) -> str:
    msg = MIMEMultipart("alternative")
    msg["From"] = f"{from_name} <{from_email}>"
    msg["To"] = TARGET_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")
    return raw


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template_string(HTML_DASHBOARD)


@app.route("/inject", methods=["POST"])
def inject_emails():
    try:
        service = get_gmail_service()
        injected = 0
        errors = []

        for i in range(50):
            data = generate_email(i)
            raw = build_raw_message(
                data["from_name"], data["from_email"], data["subject"], data["body"]
            )
            try:
                service.users().messages().insert(
                    userId="me",
                    body={"labelIds": ["INBOX", "UNREAD"], "raw": raw},
                ).execute()
                injected += 1
            except HttpError as e:
                errors.append(str(e))

        return jsonify({
            "success": True,
            "injected": injected,
            "errors": errors,
            "message": f"Successfully injected {injected} emails into inbox.",
        })
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@app.route("/reset", methods=["POST"])
def reset_inbox():
    try:
        service = get_gmail_service()
        deleted = 0

        # Page through all inbox messages and batch-delete
        page_token = None
        message_ids = []

        while True:
            params = {"userId": "me", "labelIds": ["INBOX"], "maxResults": 500}
            if page_token:
                params["pageToken"] = page_token
            result = service.users().messages().list(**params).execute()
            messages = result.get("messages", [])
            message_ids.extend([m["id"] for m in messages])
            page_token = result.get("nextPageToken")
            if not page_token:
                break

        if not message_ids:
            return jsonify({"success": True, "deleted": 0, "message": "Inbox already empty."})

        # batchDelete accepts up to 1000 IDs at a time
        chunk_size = 1000
        for i in range(0, len(message_ids), chunk_size):
            chunk = message_ids[i : i + chunk_size]
            service.users().messages().batchDelete(
                userId="me", body={"ids": chunk}
            ).execute()
            deleted += len(chunk)

        return jsonify({
            "success": True,
            "deleted": deleted,
            "message": f"Deleted {deleted} messages. Inbox is now clean.",
        })
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


# ---------------------------------------------------------------------------
# Inline HTML dashboard
# ---------------------------------------------------------------------------

HTML_DASHBOARD = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Elron Inbox Simulator</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0f0f13;
      color: #e8e8f0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 2rem;
      padding: 2rem;
    }

    .logo {
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: #8888aa;
    }

    h1 {
      font-size: 2rem;
      font-weight: 700;
      text-align: center;
      background: linear-gradient(135deg, #a78bfa, #60a5fa);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    p.subtitle {
      color: #8888aa;
      text-align: center;
      font-size: 0.95rem;
    }

    .card-grid {
      display: flex;
      gap: 1.5rem;
      flex-wrap: wrap;
      justify-content: center;
    }

    .card {
      background: #1a1a24;
      border: 1px solid #2a2a3a;
      border-radius: 16px;
      padding: 2.5rem 2rem;
      width: 260px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1rem;
      transition: border-color 0.2s;
    }
    .card:hover { border-color: #4a4a6a; }

    .card-icon { font-size: 2.5rem; }
    .card-title { font-size: 1rem; font-weight: 600; text-align: center; }
    .card-desc { font-size: 0.82rem; color: #8888aa; text-align: center; line-height: 1.5; }

    button {
      margin-top: 0.5rem;
      width: 100%;
      padding: 0.75rem 1.5rem;
      border: none;
      border-radius: 10px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: opacity 0.2s, transform 0.1s;
    }
    button:active { transform: scale(0.97); }
    button:disabled { opacity: 0.5; cursor: not-allowed; }

    .btn-inject {
      background: linear-gradient(135deg, #7c3aed, #2563eb);
      color: #fff;
    }
    .btn-reset {
      background: linear-gradient(135deg, #dc2626, #b45309);
      color: #fff;
    }

    #status {
      max-width: 480px;
      width: 100%;
      padding: 1rem 1.25rem;
      border-radius: 10px;
      font-size: 0.88rem;
      text-align: center;
      display: none;
    }
    #status.info  { background: #1e2a3a; border: 1px solid #2a4a6a; color: #93c5fd; }
    #status.ok    { background: #1a2e1a; border: 1px solid #2a5a2a; color: #86efac; }
    #status.error { background: #2e1a1a; border: 1px solid #5a2a2a; color: #fca5a5; }

    .spinner {
      display: inline-block;
      width: 14px; height: 14px;
      border: 2px solid rgba(255,255,255,0.3);
      border-top-color: #fff;
      border-radius: 50%;
      animation: spin 0.7s linear infinite;
      vertical-align: middle;
      margin-right: 6px;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
  </style>
</head>
<body>

  <div class="logo">Elron AI &mdash; Demo Tools</div>

  <h1>Inbox Simulator</h1>
  <p class="subtitle">Populate or reset the Gmail inbox for <strong>relaylegacy@gmail.com</strong></p>

  <div class="card-grid">

    <div class="card">
      <div class="card-icon">📬</div>
      <div class="card-title">Inject 50 Morning Emails</div>
      <div class="card-desc">
        Floods the inbox with realistic property management emails — maintenance requests,
        late rent, lease renewals, noise complaints & contractor quotes.
      </div>
      <button class="btn-inject" onclick="runAction('/inject', this)">
        Inject 50 Emails
      </button>
    </div>

    <div class="card">
      <div class="card-icon">🗑️</div>
      <div class="card-title">Reset / Clear Inbox</div>
      <div class="card-desc">
        Permanently deletes every message currently in the inbox, restoring a
        clean slate for the next demo run.
      </div>
      <button class="btn-reset" onclick="runAction('/reset', this)">
        Clear Inbox
      </button>
    </div>

  </div>

  <div id="status"></div>

  <script>
    async function runAction(url, btn) {
      const status = document.getElementById('status');
      const allBtns = document.querySelectorAll('button');

      allBtns.forEach(b => b.disabled = true);
      status.className = 'info';
      status.style.display = 'block';
      status.innerHTML = '<span class="spinner"></span> Working… this may take a few seconds.';

      try {
        const res = await fetch(url, { method: 'POST' });
        const data = await res.json();
        if (data.success) {
          status.className = 'ok';
          status.textContent = '✓ ' + data.message;
        } else {
          status.className = 'error';
          status.textContent = '✗ ' + data.message;
        }
      } catch (err) {
        status.className = 'error';
        status.textContent = '✗ Network error: ' + err.message;
      } finally {
        allBtns.forEach(b => b.disabled = false);
      }
    }
  </script>

</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(debug=False, port=port)
