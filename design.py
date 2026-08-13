css = '''
<style>
.chat-message {
    padding: 1rem 1.2rem;
    border-radius: 1rem;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 12px;
}

.chat-message.user {
    justify-content: flex-end;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 1rem 1rem 0.25rem 1rem;
}

.chat-message.bot {
    background: #1f2937;
    border-radius: 1rem 1rem 1rem 0.25rem;
}

.chat-message .avatar {
    width: 20%;
}

.chat-message .avatar img {
    max-width: 55px;
    max-height: 55px;
    width: 55px;
    height: 55px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid rgba(255,255,255,0.2);
}

.chat-message .message {
    width: 80%;
    padding: 0 1rem;
    color: #ffffff;
    font-size: 15px;
    line-height: 1.5;
}

.chat-message.user .message {
    text-align: right;
}

.chat-message.bot .message {
    text-align: left;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">✨</div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="message" style="text-align:right">{{MSG}}</div>
    <div class="avatar">🧑</div>    
    
</div>
'''
