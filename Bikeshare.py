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
    city = input("Please Select one of the city between Chicago, New York City or Washington: ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        print('Not Valid')
        city = input("Please Select one of the city between Chicago, New York City or Washington again: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please Select the month between January to June or all: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print('Not Valid')
        month = input("Please Select the month between January to June again: ").lower()
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please Select the day of the week or all: ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print('Not Valid')
        day = input("Please Select the day of the week again: ").lower()


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

 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df["combination"] = df['Start Station'].astype(str) + ' to ' + df['End Station']
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        
        df = df[df['day_of_week'] == day.title()]

    return df

        
         
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # TO DO: display the most common month
    print("The most common month is ", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("The most common day of week  is ", df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour
    print("The most common start hour is ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print("The most commonly used start station is ", df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is ", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
 
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0] ,"\n")
    
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time : ', total_travel_time, 'seconds.')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean of travel time : ', mean_travel_time, 'seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    
    print('Counts of user types:\n', counts_user_types, '\n')


    if 'Gender' in df:
        counts_gender = df['Gender'].value_counts()
        print('Counts of gender:\n', counts_gender, '\n')
    else:
        print('There is no information in Gender')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yob = int(df['Birth Year'].min())
        most_recent_yob = int(df['Birth Year'].max())
        most_common_yob = int(df['Birth Year'].mode())
        print('Earliest year of birth: ', earliest_yob)
        print('Most recent year of birth: ', most_recent_yob)
        print('Most common year of birth: ', most_common_yob)
    else:
        print('There is no information in Birth Year')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    x=1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
