import pandas as pd
import matplotlib.pyplot as plt

# Use raw string for file path
df = pd.read_csv(r'C:\Users\mbabd\Desktop\excavve.csv')

# Calculate the difference between expected and actual encoder readings
for i in range(5):
    df[f'Difference_Joint_{i}_Angle'] = df[f'Joint_{i}_Angle'] - df[f'Joint_{i}_Encoder']

# Plot the differences
plt.figure(figsize=(10,6))
for i in range(5):
    plt.plot(df[f'Difference_Joint_{i}_Angle'], label=f'Difference Joint {i}')
    
plt.title('Difference between Expected and Actual Encoder Readings')
plt.xlabel('Time Step')
plt.ylabel('Difference (radians)')
plt.legend()
plt.show()

# Calculate the mean and standard deviation of differences
mean_differences = df[[f'Difference_Joint_{i}_Angle' for i in range(5)]].mean()
std_differences = df[[f'Difference_Joint_{i}_Angle' for i in range(5)]].std()

# Print the results
print("Mean Differences:\n", mean_differences)
print("\nStandard Deviations:\n", std_differences)
