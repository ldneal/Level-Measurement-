import random
import time

def measure_distance():
    """
    Simulates measuring the distance by generating random values
    within a predefined range (e.g., 5 to 400 cm).
    """
    distance = random.uniform(5.0, 400.0)  # Simulate distance in cm
    return round(distance, 2)

def main():
    try:
        print("Simulating level measurement...")
        while True:
            distance = measure_distance()
            print(f"Measured Distance: {distance} cm")
            
            # Determine level
            if distance < 50:
                print("Warning: Low level detected!")
            elif distance > 350:
                print("Warning: Overflow risk detected!")
            else:
                print("Level is normal.")
                break

            time.sleep(1)  # Wait for a second before simulating again
    except KeyboardInterrupt:
        print("Simulation stopped by user")

if __name__ == "__main__":
    main()
