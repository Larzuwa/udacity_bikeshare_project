import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_SELECTION= ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY_SELECTION = ['monday', 'tuesday', 'wednesday', 'thursday',
            'friday', 'saturday', 'sunday', 'all']

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
    city = ""
    while city not in CITY_DATA:
        city = input("\nFor what city do you want to select data: "
                      "New York City, Chicago or Washington?\n>").strip().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in MONTH_SELECTION:
        month = input("\nFor which month do you want to select data?"
                      "\nEnter the month's name or alternatively enter 'all'\n>").strip().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day not in DAY_SELECTION:
        day = input("\nFor which day do you want to display the information?"
                      "\nEnter the week's day name or alternatively enter 'all'\n>")strip().lower()


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

    # Extract time information to create columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable (not all selected)
    if month != 'all':
       # create list with all the months for which we have data
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # convert the month to an integer in order to be able to filter
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    # filter by day of week if applicable (not selected all)
    if day != 'all':
        df = df[df['Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # create a tuplate that relates the number with the month name
    look_up = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
        '6': 'June'}
    common_month = df['Month'].mode()[0]
    month_to_string = look_up[str(common_month)]
    print("The most common month of the year is: {}".format(month_to_string))

    # TO DO: display the most common day of week
    popular_day = df['Day'].mode()[0]
    print("The most common day of the week is: {}".format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['Start Hour'].mode()[0]
    print('The most common start hour is: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trips...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = str(df['Start Station'].mode()[0])
    print("The most commonly used Start Station is: {}".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = str(df['End Station'].mode()[0])
    print("The most commonly used End Station is: {}".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Combination'] = (df['Start Station'] + ' - ' +
                                   df['End Station'])
    most_common_start_end_combination = str(df['Start-End Combination']
                                            .mode()[0])
    print("The most frequent combination of start and end stations is: \n{}".format(most_common_start_end_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # Sum all the values for the Trip Duration field
    total_time = df['Trip Duration'].sum()
    # Dividing by seconds in a day to get the number of days
    total_time = (str(int(total_time//86400)) +
                         'd ' +
    # Dividing by seconds in one hour to get the number of hours
                         str(int((total_time % 86400)//3600)) +
                         'h ' +
    # Dividing by number of minutes in one hour to get the number of hours
                         str(int(((total_time % 86400) % 3600)//60)) +
                         'm ' +
    # Dividing by number of seconds in one minute to get the number of seconds
                         str(int(((total_time % 86400) % 3600) % 60)) +
                         's')
    print('The total travel time is: {}'.format(total_time))


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    mean_time = (str(int(mean_time//60)) + 'm ' +
                        str(int(mean_time % 60)) + 's')
    print("The mean travel time is: {}".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Counts of user types: \n{}".format(user_types))

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts().to_string()
        print("\nCounts of gender: \n{}".format(gender_counts))
    except KeyError:
        print("No data was retrieved")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nThe earliest year of birth is: {}".format(earliest_birth_year))

        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("The most recent year of birth is: {}".format(most_recent_birth_year))

        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("The most common year of birth is: {}".format(most_common_birth_year))
    except:
        print("No data was retrieved")

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
