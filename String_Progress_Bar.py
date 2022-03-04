
#Attempts to import the progress bar
try:
    import Progress_Bar as Bar #For running the file by itself
except:
    from Terminal_Progress_Bar import Progress_Bar as Bar #for when this file gets imported by another

class StringBar(Bar.ProgressBar):
    """
    Extends the Progress_Bar.ProgressBar() class, turning the output into a string instead of sending it directly to the terminal. This version of the progress bar cannot be edited once it is created and uses the default symbols, but is much easier to use in other files, only requiring one command to run: StringBar(length=50, percent=0).to_string()

    Methods
    -------
    add_percent(percent)
        A simplified version of Progress_Bar.ProgressBar()'s add_percent(), it simply sets the percent
    to_string()
        Returns a string value of the progress bar, including the divider bars above and below it
    """

    def __init__(self, length=50, percent=0):
        """
        Creates the progress bar and turns it into a string.

        Parameters
        ----------
        bar_length : int, optional
            The length of the bar, in characters
        percent : float, optional
            The percent full the bar starts with
        """

        #uses Progress_Bar.ProgressBar()'s __init__()
        Bar.ProgressBar.__init__(self, length, percent)

        #String version of the progress bar
        self.final_bar = f"{self._replace_symbols()}\n\n   {self.bar} - {round(float(self.percent), 2)}%\n\n{self._replace_symbols()}\n"
        
    def add_percent(self, percent):
        """
        A simplified version of Progress_Bar.ProgressBar()'s add_percent, it sets the percent of the progress bar. Is called by Progress_Bar.ProgressBar()'s __init() method, overriding the original add_percent()

        Parameters
        ----------
        percent : float
            The percent by which to change the progress bar. Can be between -100.00 and 100.00, but will not overfill or underfill the bar.
        """

        round_by = round(abs((percent / (100 / self.bar_length)) - self._num_x))
        self.bar = self.bar.replace(self.empty_symbol, self.symbol, round_by)

    def to_string(self):
        """
        Returns
        -------
            A string version of the progress bar
        """

        return self.final_bar

if (__name__ == '__main__'):
    test = StringBar(20, 50).to_string()
    print(test)