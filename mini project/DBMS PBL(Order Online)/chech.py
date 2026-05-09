import razorpay
keyid = 'rzp_test_zck2ZfCUELkkGE'
keysecret = 'IB8RSwmato54taNe3cRdKJgL'
client = razorpay.Client(auth=(keyid, keysecret))

data = {"amount": 500*100, "currency": "INR", "receipt": "order_rcptid_11"}
payment = client.order.create(data=data)
print(payment)

'''
client.utility.verify_payment_signature({
        'razorpay_order_id': "pay_Lgmdbo4oMMRh9A",
        'razorpay_payment_id': "order_Lgmd1KeuDzyysP",
        'razorpay_signature': "01c85de25b619880b988d8147d6b390d2d103a196126e2bd17fef0ff0995fd25"
    })
'''