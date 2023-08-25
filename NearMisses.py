"""
Title           : Fermat’s Last Theorem Near Misses
File Name       : NearMisses.py
Name            :
Email           :
Course Number   :
Section Number  :
Date            : 23-08-2023
Explanation     : The program works based on computation and finds the best near miss for a provided equation involving exponentiation.The user is asked to provide input for variables ‘n’ and ‘k’. Based on the given input, the program performs a searching operation for a combination of ‘x’, ‘y’ and ‘z’. The result of this operation provides the smallest relative miss based on the defined equation.
"""

# Function to calculate the relative miss
def calculate_miss(x, y, z, n):
    target = x**n + y**n
    miss = min(abs(target - z**n), abs((z+1)**n - target))
    RelativeMisses = (miss / target) * 100
    return miss, RelativeMisses

# Function to find the best near misses
def find_nearestmisses(n, k):
    # Initialize variables
    Smallest_RelativeMisses = float('inf')
    bestX, bestY, bestZ = None, None, None

    for x in range(10, k+1):
        for y in range(10, k+1):
            for z in range(1, k+1):
                
                # Calculate the miss and relative miss
                miss, RelativeMisses = calculate_miss(x, y, z, n)
                
                # Update best near miss
                if RelativeMisses < Smallest_RelativeMisses:
                    Smallest_RelativeMisses = RelativeMisses
                    bestX, bestY, bestZ = x, y, z

    return bestX, bestY, bestZ, Smallest_RelativeMisses
    
# Main function 
def main():
    print("Welcome to Fermat's Last Theorem Near Misses\n")
    # Get user input
    n = int(input("Enter the n Value,n must be greater than 2 and less than 12:"))
    k = int(input("\nEnter the K Value, must be greater than 10:"))
    
    # Check if input values are valid
    if 2 < n < 12 and k > 10:
        bestX, bestY, bestZ, Smallest_RelativeMisses = find_nearestmisses(n, k)
        
        # Display output
        print("\nBest near miss:")
        print(f"x: {bestX}, y: {bestY}, z: {bestZ}")
        print(f"Actual miss: {calculate_miss(bestX, bestY, bestZ, n)[0]}")
        print(f"Relative miss: {Smallest_RelativeMisses:.2f}%")
    else:
        print("Invalid input. Please make sure n is between 2 and 12, and k is greater than 10.")

if __name__ == "__main__":
    main()
