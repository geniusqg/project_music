# -*- coding: utf-8 -*-

from zope.interface import implementer
from scrapy.extensions.feedexport import FileFeedStorage,IFeedStorage

@implementer(IFeedStorage)
class NewFileFeedStorage(FileFeedStorage):
    '''rewrite FileFeedStorage method:open(),change open file method to wb'''

    def open(self, spider):
        super(NewFileFeedStorage,self).open(spider)
        return open(self.path, 'wb')



