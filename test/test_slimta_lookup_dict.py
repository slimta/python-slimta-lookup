
from mox import MoxTestBase, IsA

from slimta.lookup.drivers.dict import DictLookup


class TestDictLookup(MoxTestBase):

    def setUp(self):
        super(TestDictLookup, self).setUp()
        test = {'test one two': 1, 'test three four': 2}
        self.drv = DictLookup(test, 'test {a} {b}')

    def test_lookup_miss(self):
        self.assertEqual(None, self.drv.lookup(a='one', b='four'))
        self.assertEqual(None, self.drv.lookup(a='three', b='two'))

    def test_lookup_hit(self):
        self.assertEqual(1, self.drv.lookup(a='one', b='two'))
        self.assertEqual(2, self.drv.lookup(a='three', b='four'))


# vim:et:fdm=marker:sts=4:sw=4:ts=4
