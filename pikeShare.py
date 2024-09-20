import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
    retry_limit = 3

    # Handle city input
    city_attempts = 0
    while True:
        city = input("Please enter the city (Chicago, New York City, Washington): ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            city_attempts += 1
            print("Invalid input. Please enter either Chicago, New York City, or Washington.")
            if city_attempts >= retry_limit:
                print("Too many invalid attempts. Exiting...")
                exit()
    
    # Handle month input
    month_attempts = 0
    while True:
        month = input("Please enter the month (January, February, ..., June) or 'all' for no filter: ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            month_attempts += 1
            print("Invalid input. Please enter a valid month from January to June, or 'all'.")
            if month_attempts >= retry_limit:
                print("Too many invalid attempts. Exiting...")
                exit()
    
    # Handle day input
    day_attempts = 0
    while True:
        day = input("Please enter the day of the week (Monday, Tuesday, ..., Sunday) or 'all' for no filter: ").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            day_attempts += 1
            print("Invalid input. Please enter a valid day of the week or 'all'.")
            if day_attempts >= retry_limit:
                print("Too many invalid attempts. Exiting...")
                exit()

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
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    popular_month = df['month'].mode()[0]
    print('Most Popular Start month:', popular_month)


    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Start day of week:', popular_day_of_week)


    # TO DO: display the most common start hour
    
    ## extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    ## find the most popular hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End comb'] = df['Start Station'] + " to " + df['End Station']
    popular_trip = df['Start-End comb'].mode()[0]
    print('Most Frequent Trip: from', popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time, 'seconds')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time, 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types')
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:')
        print(gender_counts)
    else:
        print('\nNo Gender data available.')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])

        print('\nEarliest Year of Birth:', earliest_year)
        print('Most Recent Year of Birth:', most_recent_year)
        print('Most Common Year of Birth:', most_common_year)
    else:
        print('\nNo Birth Year data available.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays 5 rows of raw data at a time based on user input."""
    start_row = 0  # Initialize the starting row index
    end_row = 5    # Number of rows to display at a time
    
    while True:
        # Ask the user if they want to see raw data
        show_data = input('\nWould you like to see 5 rows of raw data? Enter yes or no: ').lower()
        
        # If user says 'yes', display 5 rows of data
        if show_data == 'yes':
            print(df.iloc[start_row:end_row])
            start_row += 5
            end_row += 5
            
            # If we've reached the end of the data, break out of the loop
            if start_row >= len(df):
                print("\nYou've reached the end of the data.")
                break
        # If the user says 'no', exit the loop
        elif show_data == 'no':
            print("\nYou chose not to display more raw data.")
            break
        # Handle invalid input
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")

def main():
    pd.set_option('display.max_columns', None)  # This will display all columns
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
