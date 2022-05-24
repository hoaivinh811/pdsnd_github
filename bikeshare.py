import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    city_list = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Please choose the city: chicago, new york city, washington\n").lower()
        if city not in city_list:
            print('You input the wrong city')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = None
    while True:
        month = input("Please choose the month: 'all', 'january', 'february', 'march', 'april', 'may', 'june'\n").lower()
        if month not in months and month != 'all':
            print('You input the wrong month')
        else:
            break
    if month != 'all':
        month = months.index(month) + 1

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = None
    while True:
        day = input("Please choose the day: 'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'\n").lower()
        if day not in days:
            print('You input the wrong day')
        else:
            break

    print('-'*40)
    return city, month, day


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
    
    #Transform time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter out for month and day
    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month:', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('The most common day of week:', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('The most common start hour:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station:', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('The most commonly used end station:', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip:')
    print("Start: '" + (df['Start Station'] + "'. End: '" + df['End Station']).mode()[0] + "'")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The mean travel time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types:")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # In case of Washington, there's no Gender column so we will by pass
    if 'Gender' in df:
        print("The counts of gender:")
        print(df['Gender'].value_counts())
    else:
        print('No information about Gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    # In case of Washington, there's no Gender column so we will by pass
    if 'Birth Year' in df:
        print('The earliest year of birth:', df['Birth Year'].min())
        print('The most recent year of birth:', df['Birth Year'].max())
        print('The most common year of birth:', df['Birth Year'].mode()[0])
    else:
        print('No information about Birth Year')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes to view or input any key to exit\n')
    if view_data == 'yes':    
        start_loc = 0
        print(df.iloc[start_loc : start_loc +5])
        start_loc += 5
        while (view_data == 'yes') & (start_loc < len(df.index)):
            view_data = input("Do you wish to view the next 5 rows of individual trip data?\n: yes to continue or input any key to exit\n").lower()
            if view_data == 'yes':
                print(df.iloc[start_loc : start_loc +5])
                start_loc += 5
        else:
            print('All the data is displayed')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

