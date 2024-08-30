import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
FILTER_CHOICES = ['Month', 'Both', 'None', 'Day']

def get_month():
    while True:
        try:
            month = input("\nWhich month's report would you like to see? Choose number 1 to 6 (e.g. 1 = Jan, 2 = Feb... 6 = Jun)")
            if int(month.strip()) > len(MONTHS) or int(month.strip()) < 1:
                print("Incorrect Input! Please choose the correct month's number\n")
                continue
        except Exception as e:
            print("Incorrect Input! Please choose the correct month's number\n")
            continue
        break
    return MONTHS[int(month)-1]

def get_day():
    while True:
        try:
            day = input("\nWhich day's report would you like to see? Choose number 1 to 7 (e.g. 1 = Sun, 2 = Mon... 7 = Sat)")
            if int(day.strip()) > len(DAYS) or int(day.strip()) < 1:
                print("Incorrect Input! Please choose the correct day's number\n")
                continue
        except Exception as e:
            print("Incorrect Input! Please choose the correct day's number\n")
            continue
        break
    return DAYS[int(day)-1]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        try:
            city = input("\nWhich city report would you like to see? \n1. Chicago   2. New York City    3. Washington :\n Enter number: ")
            if int(city.strip()) > len(CITIES) or int(city.strip()) < 1:
                print("\nIncorrect Input! Please choose correct city's number!\n")
                continue
        except Exception as e:
            print("Incorrect Input! Please choose the correct city's number\n")
            continue
        break
    city = CITIES[int(city)-1]

    while True:
        try:
            filter_choice = input("\n Would you like to filter report based on month, day, both or none? Type 'None' for no filter: \n").capitalize()
            if filter_choice not in FILTER_CHOICES:
                print("Incorrect Input! Please choose the correct option\n")
                continue
        except Exception as e:
            print("Incorrect Input! Please choose the correct option\n")
            continue
        break

    match filter_choice:
        case 'None':
            return city, 'all', 'all'
        case 'Both':
            return city, get_month(), get_day()
        case 'Month':
            return city, get_month(), 'all'
        case 'Day':
            return city, 'all', get_day()

    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)

    print('-'*40)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':   
        month = MONTHS.index(month) + 1

        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most common month of Travel: {common_month}")
    print(f"Count: {df['month'].value_counts()[common_month]}\n")

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of Travel: {common_day}")
    print(f"Count: {df['day_of_week'].value_counts()[common_day]}\n")

    # display the most common start hour
    hours = df['Start Time'].dt.hour
    common_hour = hours.mode()[0]
    print(f"Most common hour of Travel: {common_hour}")
    print(f"Count: {hours.value_counts()[common_hour]}\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print(f"Most common Start Station: {common_start_st}")
    print(f"Count: {df['Start Station'].value_counts()[common_start_st]}\n")
    


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most common End Station: {common_end_station}")
    print(f"Count: {df['End Station'].value_counts()[common_end_station]}\n")


    # display most frequent combination of start station and end station trip
    combination = pd.concat([df['Start Station'], df['End Station']])
    comb_mode = combination.mode()[0]
    
    print(f"Most common combination of Start and End Station: {comb_mode}")
    print(f"Count: {combination.value_counts()[comb_mode]}\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f"Total time to travel: {df['Trip Duration'].sum()}\n")


    # display mean travel time
    print(f"Average time to travel: {df['Trip Duration'].mean()}\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(f"Total number of users based on types: \n{df['User Type'].value_counts()}\n")


    # Display counts of gender
    if "Gender" in df.columns:
        print(f"Total number of users based on types: \n{df['Gender'].value_counts()}\n")
    else:
        print("There is no gender data")



    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print(f"Earliest birth year: {df['Birth Year'].min()}\n")
        print(f"Most recent birth year: {df['Birth Year'].max()}\n")
        print(f"Most common birth year: {df['Birth Year'].mode()[0]}\n")
    else:
        print("There is no Birth year data")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)

        """
        - Filling Nan values in column Gender and Birth year as other columns doesn't have Nan values. 
        - Because dropping those values will leave us with only one User Type (but it will also lead to biased data when it comes to Gender and Bith year)
        - We can always go with other types of data imputation here ()
        - As Washington.csv doesnt have columns Gender and Birth Year, we need to put the check
        """

        if "Gender" in df.columns:
            df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
        if "Birth Year" in df.columns:
            df['Birth Year'] = df['Birth Year'].fillna(df['Birth Year'].median()).astype('int64')

        print(df.head(10))

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
