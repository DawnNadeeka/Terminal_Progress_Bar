class ProgressBar():
    """
    A class used to display a progress bar in the terminal, with a customizable appearance and methods to alter the current percentage. WARNING: Printing anything to the terminal while the progress bar is open will cause it to display weirdly; avoid printing while it is running, and close the bar once you are finished with it with ProgressBar.end()

    Methods
    -------
    show()
        Displays the progress bar in the terminal
    symbol()
        The symbol used for the filled portion of the progress bar
    empty_symbol()
        Symbol used for the empty portion of the progress bar
    edge_front()
        The symbol for the opening of the bars
    edge_back()
        The symbol for the closing of the bars
    add_percent(percent)
        Increses or decreases the progress bar by the given percent
    end()
        Closes the progress bar by putting an ending bar, making it so that the bar can no longer be edited
    is_open()
        Returns whether the bar is open for editing
    """

    def __init__(self, bar_length=50, percent=0):
        """
        Initializes the progress bar with default symbols

        Parameters
        ----------
        bar_length : int, optional
            The length of the bar, in characters
        percent : float, optional
            The percent full the bar starts with
        """

        self.bar = ""

        #Symbols to be used for the display
        if bar_length < 0:
            raise ValueError("bar_length must be a positive integer")
        self.bar_length = bar_length 

        if percent < -100 or percent > 100:
            raise ValueError("percent must be a decimal between -100 and 100")
        self.percent = percent
        
        #Default symbols
        self._symbol = "█"
        self._empty_symbol = "░"
        self._edge_front = "["
        self._edge_back = "]"
        self._divider = "-"

        #Fills display to be empty
        self.bar = self.edge_front
        for i in range(self.bar_length):
            self.bar += self.empty_symbol
        self.bar += self.edge_back

        self._num_x = 0
        self._is_open = True
        self._bar_displayed = False

        self.add_percent(self.percent)

    #region "Setters and getters for progress bar symbols"
    @property
    def symbol(self):
        """
        The symbol used for the filled portion of the progress bar
        
        Parameters
        ----------
        symbol : str
            Any ASCII character

        Raises
        ------
        ValueError
            If the symbol is not exactly one character long, or is already being used as another part of the progess bar
        PermissionError
            If the bar has been closed and is no longer usable
        """

        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        if not self._is_open:
            raise PermissionError("show() cannot be performed on this progress bar: bar has been closed for editing.")

        if not len(symbol) == 1:
            raise ValueError("Symbol must be one character in length")
        if (symbol == self.empty_symbol) or (symbol == self.edge_back) or (symbol == self.edge_front) or (symbol == self.divider):
            raise ValueError("Symbol is already in use")

        self.bar = self.bar.replace(self.symbol, symbol)
        self._symbol = symbol

    @property
    def empty_symbol(self):
        """
        Symbol used for the empty portion of the progress bar

        Parameters
        ----------
        empty_symbol : str
            Any ASCII character
        
        Raises
        ------
        ValueError
            If the symbol is not exactly one character long, or is already being used as another part of the progess bar
        PermissionError
            If the bar has been closed and is no longer usable
        """

        return self._empty_symbol

    @empty_symbol.setter
    def empty_symbol(self, empty_symbol):
        if not self._is_open:
            raise PermissionError("show() cannot be performed on this progress bar: bar has been closed for editing.")

        if not len(empty_symbol) == 1:
            raise ValueError("Symbol must be one character in length")
        if (empty_symbol == self.symbol) or (empty_symbol == self.edge_back) or (empty_symbol == self.edge_front) or (empty_symbol == self.divider):
            raise ValueError("Symbol is already in use")
        
        self.bar = self.bar.replace(self.empty_symbol, empty_symbol)
        self._empty_symbol = empty_symbol

    @property
    def edge_front(self):
        """
        The symbol for the opening of the bars

        Parameters
        ----------
        edge_front : str
            Any ASCII character
        
        Raises
        ------
        ValueError
            If the symbol is not exactly one character long, or is already being used as another part of the progess bar
        PermissionError
            If the bar has been closed and is no longer usable
        """

        return self._edge_front

    @edge_front.setter
    def edge_front(self, edge_front):
        if not self._is_open:
            raise PermissionError("show() cannot be performed on this progress bar: bar has been closed for editing.")

        if not len(edge_front) == 1:
            raise ValueError("Symbol must be one character in length")
        if (edge_front == self.symbol) or (edge_front == self.empty_symbol) or (edge_front == self.edge_back) or (edge_front == self.divider):
            raise ValueError("Symbol is already in use")
        
        self.bar = self.bar.replace(self.edge_front, edge_front)
        self._edge_front = edge_front
    
    @property
    def edge_back(self):
        """
        The symbol for the closing of the bars

        Parameters
        ----------
        edge_back : str
            Any ASCII character

        Raises
        ------
        ValueError
            If the symbol is not exactly one character long, or is already being used as another part of the progess bar
        PermissionError
            If the bar has been closed and is no longer usable
        """

        return self._edge_back

    @edge_back.setter
    def edge_back(self, edge_back):
        if not self._is_open:
            raise PermissionError("show() cannot be performed on this progress bar: bar has been closed for editing.")

        if not len(edge_back) == 1:
            raise ValueError("Symbol must be one character in length")
        if (edge_back == self.symbol) or (edge_back == self.empty_symbol) or (edge_back == self.edge_front) or (edge_back == self.divider):
            raise ValueError("Symbol is already in use")
        
        self.bar = self.bar.replace(self.edge_back, edge_back)
        self._edge_back = edge_back
    
    @property
    def divider(self):
        """
        The symbol for the dividers

        Parameters
        ----------
        edge_front : str
            Any ASCII character
        
        Raises
        ------
        ValueError
            If the symbol is not exactly one character long, or is already being used as another part of the progess bar
        PermissionError
            If the bar has been closed and is no longer usable
        """

        return self._divider

    @divider.setter
    def divider(self, divider):
        if not self._is_open:
            raise PermissionError("show() cannot be performed on this progress bar: bar has been closed for editing.")

        if not len(divider) == 1:
            raise ValueError("Symbol must be one character in length")
        if (divider == self.symbol) or (divider == self.empty_symbol) or (divider == self.edge_front) or (divider == self.edge_back):
            raise ValueError("Symbol is already in use")
        
        self.bar = self.bar.replace(self.divider, divider)
        self._divider = divider
    
    #endregion

    def show(self):
        """
        Displays the progress bar in the terminal

        Raises
        ------
        PermissionError
            If the bar has been closed and is no longer usable
        """

        if not self._is_open:
            raise PermissionError("show() cannot be performed on this progress bar: bar has been closed for editing.")

        if self._bar_displayed:
            return

        print(f"{self._replace_symbols()}\n") #Divider bar, the same length as the progress bar
        print(f"   {self.bar} - 0.0%", end="\r") #Progress bar
        self._bar_displayed = True

    def add_percent(self, percent):
        """
        Increses or decreases the progress bar by the given percent

        Parameters
        ----------
        percent : float
            The percent by which to change the progress bar. Can be between -100.00 and 100.00, but will not overfill or underfill the bar.

        Raises
        ------
        PermissionError
            If the bar has been closed and is no longer usable
        """

        if not self._is_open:
            raise PermissionError("add_percent() cannot be performed on this progress bar: bar has been closed for editing.")

        self.percent += percent
        if self.percent > 100:
            self.percent = 100
        
        if (self.percent < 0):
            self.percent = 0

        round_by = round(abs((self.percent / (100 / self.bar_length)) - self._num_x))
        if percent > 0:
            self.bar = self.bar.replace(self.empty_symbol, self.symbol, round_by)
        else:
            self.bar = self.bar[::-1].replace(self.symbol, self.empty_symbol, round_by)[::-1]

        try:
            self._num_x += (percent / abs(percent)) * round_by
        except ZeroDivisionError:
            return #Percent is 0, no change

        if not self._bar_displayed:
            self.show()

        print(f"   {self.bar} - {round(float(self.percent), 2)}%", end="\r") #Prints progress bar plus percentage, writing over the previous bar

    def end(self):
        """
        Closes the progress bar by putting an ending bar, making it so that the bar can no longer be edited
        """

        #If the bar is already closed, nothing happens
        if not self._is_open:
            return

        print(f"\n\n{self._replace_symbols()}\n") #Divider bar, the same length as the progress bar
        self._is_open = False
    
    def _replace_symbols(self):
        """
        Replaces the symbols in self.bar so that it is a simple divider bar, to be printed before and after the progress bar

        Returns
        -------
        self.bar with each symbol replaced with self.divider, excluding self.edge_front and self.edge_back
        """

        return f"{self.edge_front}{3 * self.divider}{self.bar.replace(self.edge_front, '').replace(self.edge_back, '').replace(self.empty_symbol, self.divider).replace(self.symbol, self.divider)}{13 * self.divider}{self.edge_back}"

    def is_open(self):
        """
        Returns whether the bar is open for editing
        """
        return self._is_open

def create_progress_bar(bar_length=50, percent=0):
    """
    Creates a progress bar.

    Parameters
    ----------
    bar_length : int, optional
        The length of the bar, in characters
    percent : float, optional
        The percent full the bar starts with

    Returns
    -------
        A reference to the newly created progress bar.
    """

    return ProgressBar(bar_length, percent)

if (__name__ == '__main__'):
    import examples
