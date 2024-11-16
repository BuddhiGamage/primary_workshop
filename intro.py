import qi
from connection import Connection

def generate_prompt():
    return (
        "Hello everyone! Welcome to our robotics workshop! My name is Pepper, and I'm a humanoid robot. "
        "That means I’m built to move, talk, and even think a little like humans. "
        "I’m so excited to meet all of you amazing students today! Did you know I can see, hear, and even dance? "
        "Yes, that’s right! I’m like a super cool robot friend who’s here to have fun with you and show you just how amazing robots can be. "
        "Let’s start with something cool: Have you ever wondered how robots like me can understand the world around us? "
        "I use cameras to see, microphones to hear, and a computer brain to process all the information. "
        "Pretty neat, huh? "
        "Today, we’re going to learn a little bit about robots and have some fun together. And guess what? I also love to dance! "
        "By the end of this workshop, you’ll get to see my awesome dance moves and maybe even join me. "
        "Now, I have a question for you: If you could build your own robot, what would it do? "
        "Think about it because I’d love to hear your ideas later! "
        "Alright, are you all ready to dive into the amazing world of robotics? Let’s get started!"
    )

def perform_intro():
    # behavior_mng_service = session.service("ALBehaviorManager")
    # tts_service = session.service("ALTextToSpeech")
    
    try:
        # Stop all behaviors
        behavior_mng_service.stopAllBehaviors()

        # Start the welcome behavior if available
        behavior_action = "primary_actions/welcome"
        if behavior_action in behavior_mng_service.getInstalledBehaviors():
            behavior_mng_service.startBehavior(behavior_action)
        else:
            print(f"Behavior '{behavior_action}' not found!")

        # Generate and say the prompt
        prompt = generate_prompt()
        print("Starting TTS...")
        tts_service.say(prompt)
        print("Finished TTS.")

        # Stop all behaviors after the introduction
        behavior_mng_service.stopAllBehaviors()

    except Exception as e:
        print(f"Error during Pepper's performance: {e}")
        # Stop behaviors if an error occurs
        behavior_mng_service.stopAllBehaviors()

# Connect to Pepper
pepper = Connection()
# session = pepper.connect('localhost', '43555')  # Or use your Pepper's IP and port
# session = pepper.connect('10.0.0.244', '9559')  # Or use your Pepper's IP and port
session = pepper.connect('172.20.10.4', '9559') 

# Main script execution
try:
    behavior_mng_service = session.service("ALBehaviorManager")
    tts_service = session.service("ALTextToSpeech")
    # setting parameters
    tts_service.setParameter("speed", 85)
    perform_intro()

except KeyboardInterrupt:
    print("\nKeyboardInterrupt detected. Stopping all behaviors...")
    # Stop all behaviors on Pepper if interrupted
    
    behavior_mng_service.stopAllBehaviors()    
    print("All behaviors stopped. Exiting gracefully.")