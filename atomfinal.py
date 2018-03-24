import pandas as pd
import datetime as dt
from datetime import timedelta
import time
import csv

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York City, or Washington?\n')

    # handle invalid city input
    while city.lower() not in CITY_DATA:
	print(city + ' is not a valid city.')
        city = input('\nWould you like to see data for Chicago, New York City, or Washington?\n')
	
    # handle valid city input
    print('Okay. We will explore data for ' + city.title() + '.')
    city = CITY_DATA[city.lower()]

    # get user input for month (all, january, february, ... , june)
    month = input('\nWhich month? January, February, March, April, May, June, or all?\n')
    print('Okay. We will analyze data from ' + month.title() + '.')
    # TODO: handle raw input and complete function

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhich day of the week? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all?\n')
    print('Okay. We will analyze data from ' + day.title() + '.')
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
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day_of_week'] = df['Start Time'].dt.weekday_name
	
    # filter by month if applicable
    if month.lower() != 'all':
	# filter by month to create the new dataframe
	df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
	
    # display the most common month
    # load data file into a dataframe
    df['month'] = df['Start Time'].dt.strftime('%B')
    popular_month = dfmonth.mode()[0]
    print('Most Popular Month:', popular_month)

    # display the most common day of week
    # load data file into a dataframe
    weekday_name = df['Start Time'].dt.weekday_name
    popular_day = weekday_name.mode()[0]
    print('Most Common Day of the Week:', popular_day)

    # display the most common start hour
    # load data file into a dataframe
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', start_station)

    # TODO: complete function

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', end_station)

    # display most frequent combination of start station and end station trip
    df['combined_stations']=df['Start Station'] +', '+df['End Station']
    most_common_trip = df['combined_stations'].mode()[0]
    print('Most Frequent Combination of Start Station and End Station Trip:', most_common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = pd.to_timedelta(df['Trip Duration'], unit='s')
    print(total_travel_time.sum())


    # display mean travel time
    print(total_travel_time.mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Users by Type:\n', user_types) #FIX: there is a space on the second line
    # Display counts of gender
    if 'Gender' in df:
    	gender = df['Gender'].value_counts()
    	print('Users by Gender:\n', gender) #FIX: there is a space on the second line
    else:
	print('Gender data is unavailable for this city.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
    	birth_year = df['Birth Year']
    	#Display earliest year of birth
    	earliest_year = birth_year.min()
    	print('Earliest Birth Year:', earliest_year.astype(int))
    	#Display most recent year of birth
    	recent_year = birth_year.max()
    	print('Most Recent Birth Year:', recent_year.astype(int))
    	#Display most common year of birth
    	birth_year_totals = birth_year.value_counts()
    	common_year = birth_year_totals.idxmax()
    	print('Most Common Birth Year:', common_year.astype(int))
    else:
	print('Birth year data is unavailable for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
