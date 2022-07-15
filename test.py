import dayOfWeek
import decToBinary
import noOfNotes
import timeConver


def test_timeConver():
    output = timeConver.Conversion(40)
    assert output == 4.444444444444445


def test_dayOfWeek():
    output = dayOfWeek.day_of_the_week(2017, 7, 13)
    assert output == 4


def test_noOfNotes():
    output = noOfNotes.countCurrency(500)
    assert output == (500, 1)


def test_decToBinary():
    output = decToBinary.ToBinaryConversion(10)
    assert output == 1010
