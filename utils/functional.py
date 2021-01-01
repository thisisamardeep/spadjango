class LazyObject:
    """
       A wrapper for another class that can be used to delay instantiation of the
       wrapped class.

       By subclassing, you have the opportunity to intercept and alter the
       instantiation. If you don't need to do that, use SimpleLazyObject.
       """
