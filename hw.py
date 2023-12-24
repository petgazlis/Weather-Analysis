import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r'C:\Users\paoka\OneDrive\Υπολογιστής\py\wd.csv'
df = pd.read_csv(file_path)
print("\033[1;31mΑΝΑΛΥΣΗ ΔΕΔΟΜΕΝΩΝ ΚΑΙ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ ΣΕ PYTHON 3\033[0m")
print("\033[1;32mCASE STUDY \033[0m")
print("\033[1;34mΤο αρχείο wd.csv περιέχει πραγματικά μετεωρολογικά δεδομένα (παρατηρήσεις)\
 από την περιοχή Αγία Παρασκευή Αττικής, για το έτος 2017. Χρησιμοποιώντας κατάλληλες\
 εντολές της Python και Pandas απάντησα στα παρακάτω. \033[0m")
                                                         
# Έλεγχος τύπων στοιχείων
#print(df.dtypes)
#print(df)
print("\033[1;32mΕΡΩΤΗΣΗ 1\033[0m")
print("\033[1;34mΜπορείς να το ελέγξεις βγάζοντας τη # από το script\033[0m")
# Αντικατάσταση κενών τιμών με NaN
df.replace(' ', np.nan, inplace=True)

# Μετατροπή στήλης HIGH και LOW σε float, αφού αντικαταστήσουμε τα κενά με NaN
df['HIGH'] = df['HIGH'].astype(float)
df['LOW'] = df['LOW'].astype(float)

# Κυβική παρεμβολή μόνο στα κενά των στηλών HIGH και LOW
df['HIGH'].fillna(df['HIGH'].interpolate(method='cubic', limit=3, limit_direction='both'), inplace=True)
df['LOW'].fillna(df['LOW'].interpolate(method='cubic', limit=3, limit_direction='both'), inplace=True)

# Εμφάνιση μόνο των στηλών 'HIGH' και 'LOW'
#print(df[['HIGH', 'LOW']])


# Αντικατάσταση κενών στην στήλη "MONTH" με τον χαρακτήρα "DEC"
df['MONTH'].fillna('DEC', inplace=True)
"""!ΠΡΟΣΟΧΗ!μου αφήνει ένα κενό στίς 5 Δεκ.
Το συμπληρώνω μόνος μου"""
df.at[338, 'MONTH'] = 'DEC'

# Εμφάνιση μόνο της στήλης 'MONTH'
#print(df[['MONTH']])

print("\033[1;32mΕΡΩΤΗΣΗ 2\033[0m")
print("\033[1;34mΜπορείς να το ελέγξεις βγάζοντας τη # απο το script\033[0m")
# Υπολογισμός απόλυτων τιμών για τις στήλες HIGH, LOW, και WINDHIGH
df['HIGH_ABS'] = df['HIGH'].abs()
df['LOW_ABS'] = df['LOW'].abs()
df['WINDHIGH_ABS'] = df['WINDHIGH'].abs()


# Υπολογισμός της απόλυτα μέγιστης θερμοκρασίας
absolute_max_temp = df['HIGH_ABS'].max()

# Υπολογισμός της απόλυτα ελάχιστης θερμοκρασίας
absolute_min_temp = df['LOW_ABS'].min()

# Υπολογισμός της απόλυτα ισχυρότερης έντασης ανέμου
absolute_max_wind = df['WINDHIGH_ABS'].max()

# Υπολογισμός μέσης τιμής της στήλης 'TEMP'
mean_temp = df['TEMP'].mean()

# Υπολογισμός άθροισμα της στήλης 'RAIN'
total_rain = df['RAIN'].sum()

# Υπολογισμός συνολικών (HDD)
total_hdd = df['HDD'].sum()

# Υπολογισμός συνολικών(CDD)
total_cdd = df['CDD'].sum()

# Δημιουργία νέας γραμμής με τις υπολογισμένες τιμές
new_row = {'HIGH':absolute_max_temp,'LOW': absolute_min_temp, 'WINDHIGH': [absolute_max_wind],'TEMP': mean_temp, 'RAIN': total_rain, 'HDD': total_hdd, 'CDD': total_cdd}

# Προσθήκη της νέας γραμμής στο τέλος του πίνακα
df = df.append(new_row, ignore_index=True)

print("\033[1;32mΕΡΩΤΗΣΗ 3\033[0m")
# Υπολογισμός διάμεσου
median_temperature = df['TEMP'].median()

# Υπολογισμός τυπικής απόκλισης
std_temperature = df['TEMP'].std()

# Στρογγυλοποίηση στα δύο δεκαδικά ψηφία
median_temperature = round(median_temperature, 2)
std_temperature = round(std_temperature, 2)

print("Διάμεσος μέσων θερμοκρασιών:", median_temperature)
print("Τυπική απόκλιση μέσων θερμοκρασιών:", std_temperature)

print("\033[1;32mΕΡΩΤΗΣΗ 4\033[0m")
# Υπολογισμός του αριθμού των ημερών για κάθε διεύθυνση ανέμου
wind_direction_counts = df['DIR'].value_counts()

# Δημιουργία του γραφήματος πίτας
plt.figure(figsize=(12, 10))
plt.pie(wind_direction_counts, labels=wind_direction_counts.index, autopct='%1.1f%%', startangle=1,
        pctdistance=0.8, textprops={'fontsize': 12, 'color': 'black', 'fontweight': 'bold'})
plt.axis('equal')
plt.title('Απεικόνιση κατανομής των ημερών σε διεύθυνση ανέμου που φυσούσε.', color='red', fontsize=19)
 
legend_labels = [f'{direction} ({count} ημέρες)' for direction, count in zip(wind_direction_counts.index, wind_direction_counts.values)]
plt.legend(legend_labels, loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small')

plt.show()

print("\033[1;32mΕΡΩΤΗΣΗ 5\033[0m")
# Εύρεση της ώρας που έχoουν καταγραφεί τα περισσότερα στοιχεία της στήλης 'HIGH'
hour_of_max_high_count = df['TIME'].value_counts().idxmax()

# Εύρεση της ώρας που έχου καταγραφεί τα περισσότερα στοιχεία της στήλης 'LOW'
hour_of_max_low_count = df['TIME.1'].value_counts().idxmax()

print("Η ώρα με τις περισσότερες μέγιστες θερμοκρασίες είναι:", hour_of_max_high_count)
print("Η ώρα με τις περισσότερες ελάχιστες θερμοκρασίες είναι:", hour_of_max_low_count)

print("\033[1;32mΕΡΩΤΗΣΗ 6\033[0m")
# Δημιουργούμε μια νέα στήλη με τη διαφορά των μέγιστων και ελάχιστων θερμοκρασιών
df['Temperature_Difference'] = df['HIGH'] - df['LOW']

# Αφαιρούμε τις γραμμές που περιέχουν NaN τιμές στις στήλες 'DAY', 'MONTH', 'HIGH' και 'LOW'
df_cleaned = df.dropna(subset=['DAY', 'MONTH', 'HIGH', 'LOW'])

# Βρίσκουμε την ημέρα και τον μήνα με τη μεγαλύτερη διακύμανση θερμοκρασίας
max_temperature_difference_day = df_cleaned.loc[df_cleaned['Temperature_Difference'].idxmax(), 'DAY']
max_temperature_difference_month = df_cleaned.loc[df_cleaned['Temperature_Difference'].idxmax(), 'MONTH']

print("Η μέρα με τη μεγαλύτερη διακύμανση θερμοκρασίας είναι η", max_temperature_difference_day, "μέρα του μήνα", max_temperature_difference_month)

print("\033[1;32mΕΡΩΤΗΣΗ 7\033[0m")
# Υπολογισμός του αριθμού των ημερών για κάθε διεύθυνση ανέμου
wind_direction_counts = df['DIR'].value_counts()
# Βρίσκουμε τη διεύθυνση ανέμου με τις περισσότερες ημέρες
max_wind_direction = wind_direction_counts.idxmax()

print("Καταγραφές για κάθε διεύθυνση ανέμου:")
print(wind_direction_counts)
print("Αρα, η διεύθυνση ανέμου που φύσηξε τις περισσότερες ημέρες του χρόνου είναι:", max_wind_direction)

print("\033[1;32mΕΡΩΤΗΣΗ 8\033[0m")
# Βρίσκουμε τη μέγιστη ένταση ανέμου
max_wind_speed = df['W_SPEED'].max()

# Βρίσκουμε τη διεύθυνση ανέμου που αντιστοιχεί στη μέγιστη ένταση
direction_of_max_wind_speed = df.loc[df['W_SPEED'].idxmax(), 'DIR']

print("Η διεύθυνση ανέμου με την μεγαλύτερη ένταση είναι:", direction_of_max_wind_speed)

print("\033[1;32mΕΡΩΤΗΣΗ 9\033[0m")
# Υπολογισμός μέσης θερμοκρασίας για κάθε διεύθυνση ανέμου
mean_temperature_by_wind_direction = df.groupby('DIR')['TEMP'].mean()

for direction, mean_temp in mean_temperature_by_wind_direction.items():
    print(f"Διεύθυνση ανέμου: {direction}, Μέση θερμοκρασία: {mean_temp:.2f}")

# Βρίσκουμε την μέγιστη μέση θερμοκρασία και την αντίστοιχη διεύθυνση ανέμου
max_mean_temperature_direction = mean_temperature_by_wind_direction.idxmax()
max_mean_temperature = mean_temperature_by_wind_direction.max()

# Βρίσκουμε την ελάχιστη μέση θερμοκρασία και την αντίστοιχη διεύθυνση ανέμου
min_mean_temperature_direction = mean_temperature_by_wind_direction.idxmin()
min_mean_temperature = mean_temperature_by_wind_direction.min()

print("Αρα,η Διεύθυνση ανέμου με τη μεγαλύτερη μέση θερμοκρασία:", max_mean_temperature_direction, "και μέση θερμοκρασία:", max_mean_temperature)
print("Διεύθυνση ανέμου με τη μικρότερη μέση θερμοκρασία:", min_mean_temperature_direction, "και μέση θερμοκρασία:", min_mean_temperature)

print("\033[1;32mΕΡΩΤΗΣΗ 10\033[0m")
# Λίστα με τα ονόματα των μηνών σε σωστή σειρά
months_order = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

# Υπολογισμός του αθροίσματος βροχόπτωσης ανά μήνα και ταξινόμηση με βάση τη σωστή σειρά
total_precipitation_by_month = df.groupby('MONTH')['RAIN'].sum().reindex(months_order)

plt.figure(figsize=(10, 6))
plt.bar(total_precipitation_by_month.index, total_precipitation_by_month)
plt.xlabel('Μήνας')
plt.ylabel('Βροχόπτωση (mm)')
plt.title('Κατανομή Βροχόπτωσης ανά Μήνα')
plt.xticks(rotation=45)
plt.show()

print("\033[1;32mΕΡΩΤΗΣΗ 11\033[0m")

df = df.dropna(subset=['DAY'])
# η χρονολογία είναι πάντα το 2017

# Δημιουργούμε τις πλήρεις ημερομηνίες χρησιμοποιώντας τις στήλες MONTH και DAY
dates = '2017-' + df['MONTH'] + '-' + df['DAY'].astype(int).astype(str)

# Μετατροπή σε datetime
df['DATE'] = pd.to_datetime(dates, format='%Y-%b-%d', errors='coerce')

from sklearn.linear_model import LinearRegression

df_dec_2017 = df[df['MONTH'] == 'DEC']

# Χωρίζουμε τις ημερομηνίες και τις θερμοκρασίες σε X και y
X = df_dec_2017['DATE'].dt.dayofyear.values.reshape(-1, 1)
y = df_dec_2017['TEMP'].values

# Εκτελούμε τη γραμμική παλινδρόμηση
model = LinearRegression()
model.fit(X, y)

# Προβλέπουμε τη θερμοκρασία για την 25/12/2018
day_25_dec_2018 = pd.to_datetime('2018-12-25').dayofyear
temperature_prediction = model.predict([[day_25_dec_2018]])
predicted_temperature_C = round(temperature_prediction[0], 2)
print("Η προβλεπόμενη θερμοκρασία για τις 25/12/2018 είναι:", predicted_temperature_C, "°C")

print("\033[1;32mΕΡΩΤΗΣΗ 12\033[0m")

# Φιλτράρουμε τα δεδομένα για τις εποχές
df_winter = df[(df['DATE'].dt.month >= 12) | (df['DATE'].dt.month <= 2)]
df_spring = df[(df['DATE'].dt.month >= 3) & (df['DATE'].dt.month <= 5)]
df_summer = df[(df['DATE'].dt.month >= 6) & (df['DATE'].dt.month <= 8)]
df_autumn = df[(df['DATE'].dt.month >= 9) & (df['DATE'].dt.month <= 11)]

# Υπολογίζουμε τις μέσες, μέγιστες και ελάχιστες θερμοκρασίες για κάθε εποχή
mean_winter_temp = df_winter['TEMP'].mean()
max_winter_temp = df_winter['HIGH'].max()
min_winter_temp = df_winter['LOW'].min()

mean_spring_temp = df_spring['TEMP'].mean()
max_spring_temp = df_spring['HIGH'].max()
min_spring_temp = df_spring['LOW'].min()

mean_summer_temp = df_summer['TEMP'].mean()
max_summer_temp = df_summer['HIGH'].max()
min_summer_temp = df_summer['LOW'].min()

mean_autumn_temp = df_autumn['TEMP'].mean()
max_autumn_temp = df_autumn['HIGH'].max()
min_autumn_temp = df_autumn['LOW'].min()

# Σχεδιάζουμε τις γραφικές υπο-παραστάσεις
plt.figure(figsize=(20, 12))

# Χειμώνας
plt.subplot(2, 2, 1)
plt.plot(df_winter['DATE'], df_winter['TEMP'], 'g-', label='Μέση θερμοκρασία')
plt.plot(df_winter['DATE'], df_winter['HIGH'], 'r-', label='Μέγιστη θερμοκρασία')
plt.plot(df_winter['DATE'], df_winter['LOW'], 'b-', label='Ελάχιστη θερμοκρασία')
plt.title('Χειμώνας')
plt.legend()

# Άνοιξη
plt.subplot(2, 2, 2)
plt.plot(df_spring['DATE'], df_spring['TEMP'], 'g-', label='Μέση θερμοκρασία')
plt.plot(df_spring['DATE'], df_spring['HIGH'], 'r-', label='Μέγιστη θερμοκρασία')
plt.plot(df_spring['DATE'], df_spring['LOW'], 'b-', label='Ελάχιστη θερμοκρασία')
plt.title('Άνοιξη')
plt.legend()

# Καλοκαίρι
plt.subplot(2, 2, 3)
plt.plot(df_summer['DATE'], df_summer['TEMP'], 'g-', label='Μέση θερμοκρασία')
plt.plot(df_summer['DATE'], df_summer['HIGH'], 'r-', label='Μέγιστη θερμοκρασία')
plt.plot(df_summer['DATE'], df_summer['LOW'], 'b-', label='Ελάχιστη θερμοκρασία')
plt.title('Καλοκαίρι')
plt.legend()

# Φθινόπωρο
plt.subplot(2, 2, 4)
plt.plot(df_autumn['DATE'], df_autumn['TEMP'], 'g-', label='Μέση θερμοκρασία')
plt.plot(df_autumn['DATE'], df_autumn['HIGH'], 'r-', label='Μέγιστη θερμοκρασία')
plt.plot(df_autumn['DATE'], df_autumn['LOW'], 'b-', label='Ελάχιστη θερμοκρασία')
plt.title('Φθινόπωρο')
plt.legend()

plt.tight_layout()
plt.show()

print("\033[1;32mΕΡΩΤΗΣΗ 13\033[0m")

def rain_status(total_rainfall):
    if total_rainfall < 400:
        return "Λειψυδρία"
    elif 400 <= total_rainfall < 600:
        return "Ικανοποιητικά ποσά βροχής"
    else:
        return "Υπερβολική βροχόπτωση"

total_rainfall = df['RAIN'].sum()
print("το άθροισμα των ποσών βροχόπτωσης είναι",total_rainfall)
result = rain_status(total_rainfall)
print("Κατάσταση βροχόπτωσης:", result)
