from PIL import Image
import stepic

# Load the image
image = Image.open("D:/python Data science/Forensics/hello.png")

# Secret message to encode
secret_message = "This is a secret message!hello safras pease kindly asking to decrypt this "

# Encode the message into the image
encoded_image = stepic.encode(image, secret_message.encode())

# Save the encoded image
encoded_image.save("encoded_image.png")

print("Message hidden in image successfully!")