import time
import pandas as pd
import numpy as np

#dictionary connecting city selection and city data file.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#dictionary indexing month with appropriate integer.
MONTHS = {'january' : 0,
               'february' : 1,
               'march' : 2,
               'april' : 3,
               'may' : 4,
               'june' : 5,
               'july' : 6,
               'august' : 7,
               'september' : 8,
               'october' : 9,
               'november' : 10,
               'december' : 11}

#dictionary outlining day of week with appropriate integer.
DAYS = {'monday' : 0,
             'tuesday' : 1,
             'wednesday' : 2,
             'thursday' : 3,
             'friday' : 4,
             'saturday' : 5,
             'sunday' : 6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    print('We will need to know three things:\n')
    print('1. The city that you are interested in knowing about;\n')
    print('2. The month to filter the data;\n')
    print('3. The day of the week.\n')
    print('\n If at any point, you wish to quit, simply enter "q".\n')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #Requests user input of city selection from options (will accept valid string in any format as it is formatted after user input).            Will request another input if user's selection is invalid.
    while True:
        city = input('Would you like to learn more about Chicago, New York City, or Washington?\n').lower().replace(" ","_")
        if city not in ('chicago', 'new_york_city', 'washington'):
            print('That city is not an option! Please enter another city.')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    #Requests user input of month filter selection from options (will accept valid string in any format as it is formatted after user           input). Will request another input if user's selection is invalid.
    while True:
        month = input('By which month would you like to filter? Enter "all" to apply no filter by month.\n').lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all'):
            print('That filter is not an option! Please enter another.')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Requests user input of day of week filter selection from options (will accept valid string in any format as it is formatted after         user input). Will request another input if user's selection is invalid.
    while True:
        day = input('By which day of the week would you like to filter? Enter "all" to apply no filter by day of the week.\n').lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('That filter is not an option! Please enter another.')
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

    #Upload the city file, convert each column to the correct time (dates to datetime, birth year from float to integer), and add two columns to help apply month and day of week filters
    city = city+'.csv'
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Birth Year'] = pd.to_numeric(df['Birth Year'], downcast = 'integer')
    df['start_month'] = df['Start Time'].dt.month
    df['start_day'] = df['Start Time'].dt.dayofweek

    #Applies month filter.
    if month != 'all':
        df = df[df['start_month'] == MONTHS[month]]

    #Applies day of week filter
    if day != 'all':
        df = df[df['start_day'] == DAYS[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #Calculates start month with greatest value_count()
    print("\nThe most common month is %s." % (df['start_month'].value_counts().idxmax()))

    # TO DO: display the most common day of week
    #Calculates start day with greatest value_count()
    print("\nThe most common day of the week is %s." % (df['start_day'].value_counts().idxmax()))

    # TO DO: display the most common start hour
    #Calculates start hour with greatest value_count()
    print("\nThe most common start hour is %s." % (df['Start Time'].dt.hour.value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #Calculates start station with greatest value_count()
    print("\nThe most commonly used start station is %s." % (df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    #Calculates end station with greatest value_count()
    print("\nThe most commonly used end station is %s." % (df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    #Calculates start and end station combination that occurs most in dataframe
    print("\nThe most commonly used start and end station combination is %s." % (df[['Start Station','End Station']].mode().loc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #Calculates sum() of travel time/trip duration in dataframe
    print("\nThe total travel time is %s seconds." % (df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    #Calculates mean() of travel time/trip duration in dataframe
    print("\nThe mean travel time is %s seconds." % (df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #Calculates value_counts() of user types in dataframe
    print("\nThe count of each user type is %s \n " % (df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    #Calculates value_counts() of gender in dataframe
    print("\nThe count of each gender is %s \n " % (df['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    #Calculates min(), max(), and most common (greatest value_counts()) of birth year in dataframe as integers.
    print("\nThe earliest birth year is %s.\nThe most recent birth year is %s.\nThe most common birth year is %s.\n" % (df['Birth Year'].min().astype(int), df['Birth Year'].max().astype(int), df['Birth Year'].value_counts().idxmax().astype(int)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    start_time = time.time()

    #Counts the number of rows in the datafram
    row_count = len(df.index)
    row_index = 0

    #Asks the user if they would like to see more data.
    while True and row_index<row_count:
        see_more = input("Would you like to see the raw data? Type yes for 5 more rows, or no to stop.\n")
        if see_more=="yes":
            print(df[row_index:(row_index+5)])
            row_index += 5
        else:
            break

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

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
