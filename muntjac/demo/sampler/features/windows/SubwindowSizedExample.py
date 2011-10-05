# -*- coding: utf-8 -*-


class SubwindowSizedExample(VerticalLayout):
    _subwindow = None

    def __init__(self):
        # Create the window
        self._subwindow = Window('A sized subwindow')
        self._subwindow.setWidth('500px')
        self._subwindow.setHeight('80%')
        # Configure the windws layout; by default a VerticalLayout
        layout = self._subwindow.getContent()
        layout.setMargin(True)
        layout.setSpacing(True)
        # make it fill the whole window
        layout.setSizeFull()
        # Add some content; a label and a close-button
        message = Label('This is a sized window')
        self._subwindow.addComponent(message)

        class _0_(Button.ClickListener):

            def buttonClick(self, event):
                # close the window by removing it from the parent window
                SubwindowSizedExample_this._subwindow.getParent().removeWindow(SubwindowSizedExample_this._subwindow)

        _0_ = _0_()
        close = Button('Close', _0_)
        # The components added to the window are actually added to the window's
        # layout; you can use either. Alignments are set using the layout
        layout.addComponent(close)
        layout.setComponentAlignment(close, Alignment.BOTTOM_RIGHT)
        # Add a button for opening the subwindow

        class _0_(Button.ClickListener):

            def buttonClick(self, event):
                if SubwindowSizedExample_this._subwindow.getParent() is not None:
                    # window is already showing
                    self.getWindow().showNotification('Window is already open')
                else:
                    # Open the subwindow by adding it to the parent
                    # window
                    self.getWindow().addWindow(SubwindowSizedExample_this._subwindow)

        _0_ = _0_()
        open = Button('Open sized window', _0_)
        self.addComponent(open)