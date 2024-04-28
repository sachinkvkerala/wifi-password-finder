import subprocess

def get_wifi_credentials():
    try:
        # Run the netsh command to list saved WiFi networks and their passwords
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, check=True)

        # Parse the output to extract SSIDs
        profiles = [line.split(":")[1].strip() for line in result.stdout.split("\n") if "All User Profile" in line]

        # Iterate over each SSID and retrieve the password
        for profile in profiles:
            # Run the netsh command to retrieve the password for the SSID
            password_result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True, check=True)

            # Extract the password from the output
            password_lines = password_result.stdout.split("\n")
            password_line = [line.strip() for line in password_lines if "Key Content" in line]
            if password_line:
                password = password_line[0].split(":")[1].strip()
            else:
                password = "No password set"

            # Print the SSID and password
            print(f"SSID: {profile}, Password: {password}")

    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Retrieving WiFi credentials...")
    get_wifi_credentials()
