# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdi_forms', '0029_auto_20161122_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundinfo',
            name='birth_order',
            field=models.IntegerField(verbose_name=b'Birth order', choices=[(1, b'1 (First)'), (2, b'2 (Second)'), (3, b'3 (Third)'), (4, b'4 (Fourth)'), (5, b'5 (Fifth)'), (6, b'6 (Sixth)'), (7, b'7 (Seventh)'), (8, b'8 (Eighth)'), (9, b'9 (Ninth)'), (10, b'10 or more (Tenth or Later)')]),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='birth_weight',
            field=models.FloatField(verbose_name=b'Birth weight', choices=[(0, b'Less than 3 lbs, 0 oz'), (3, b'3 lbs, 0 oz - 3 lbs, 7 oz'), (3.5, b'3 lbs, 8 oz - 3 lbs, 15 oz'), (4, b'4 lbs, 0 oz - 4 lbs, 7 oz'), (4.5, b'4 lbs, 8 oz - 4 lbs, 15 oz'), (5, b'5 lbs, 0 oz - 5 lbs, 7 oz'), (5.5, b'5 lbs, 8 oz - 5 lbs, 15 oz'), (6, b'6 lbs, 0 oz - 6 lbs, 7 oz'), (6.5, b'6 lbs, 8 oz - 6 lbs, 15 oz'), (7, b'7 lbs, 0 oz - 7 lbs, 7 oz'), (7.5, b'7 lbs, 8 oz - 7 lbs, 15 oz'), (8, b'8 lbs, 0 oz - 8 lbs, 7 oz'), (8.5, b'8 lbs, 8 oz - 8 lbs, 15 oz'), (9, b'9 lbs, 0 oz - 9 lbs, 7 oz'), (9.5, b'9 lbs, 8 oz - 9 lbs, 15 oz'), (10, b'10 lbs, 0 oz or more')]),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='father_yob',
            field=models.IntegerField(verbose_name=b"Father's (or Parent 2) Year of birth", choices=[(1950, b'1950'), (1951, b'1951'), (1952, b'1952'), (1953, b'1953'), (1954, b'1954'), (1955, b'1955'), (1956, b'1956'), (1957, b'1957'), (1958, b'1958'), (1959, b'1959'), (1960, b'1960'), (1961, b'1961'), (1962, b'1962'), (1963, b'1963'), (1964, b'1964'), (1965, b'1965'), (1966, b'1966'), (1967, b'1967'), (1968, b'1968'), (1969, b'1969'), (1970, b'1970'), (1971, b'1971'), (1972, b'1972'), (1973, b'1973'), (1974, b'1974'), (1975, b'1975'), (1976, b'1976'), (1977, b'1977'), (1978, b'1978'), (1979, b'1979'), (1980, b'1980'), (1981, b'1981'), (1982, b'1982'), (1983, b'1983'), (1984, b'1984'), (1985, b'1985'), (1986, b'1986'), (1987, b'1987'), (1988, b'1988'), (1989, b'1989'), (1990, b'1990'), (1991, b'1991'), (1992, b'1992'), (1993, b'1993'), (1994, b'1994'), (1995, b'1995'), (1996, b'1996'), (1997, b'1997'), (1998, b'1998'), (1999, b'1999'), (2000, b'2000'), (2001, b'2001'), (2002, b'2002'), (2003, b'2003'), (2004, b'2004'), (2005, b'2005'), (2006, b'2006'), (2007, b'2007'), (2008, b'2008'), (2009, b'2009'), (2010, b'2010'), (2011, b'2011'), (2012, b'2012'), (2013, b'2013'), (2014, b'2014'), (2015, b'2015'), (2016, b'2016'), (2017, b'2017'), (0, b'Prefer not to disclose')]),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='mother_yob',
            field=models.IntegerField(verbose_name=b"Mother's (or Parent 1) Year of birth", choices=[(1950, b'1950'), (1951, b'1951'), (1952, b'1952'), (1953, b'1953'), (1954, b'1954'), (1955, b'1955'), (1956, b'1956'), (1957, b'1957'), (1958, b'1958'), (1959, b'1959'), (1960, b'1960'), (1961, b'1961'), (1962, b'1962'), (1963, b'1963'), (1964, b'1964'), (1965, b'1965'), (1966, b'1966'), (1967, b'1967'), (1968, b'1968'), (1969, b'1969'), (1970, b'1970'), (1971, b'1971'), (1972, b'1972'), (1973, b'1973'), (1974, b'1974'), (1975, b'1975'), (1976, b'1976'), (1977, b'1977'), (1978, b'1978'), (1979, b'1979'), (1980, b'1980'), (1981, b'1981'), (1982, b'1982'), (1983, b'1983'), (1984, b'1984'), (1985, b'1985'), (1986, b'1986'), (1987, b'1987'), (1988, b'1988'), (1989, b'1989'), (1990, b'1990'), (1991, b'1991'), (1992, b'1992'), (1993, b'1993'), (1994, b'1994'), (1995, b'1995'), (1996, b'1996'), (1997, b'1997'), (1998, b'1998'), (1999, b'1999'), (2000, b'2000'), (2001, b'2001'), (2002, b'2002'), (2003, b'2003'), (2004, b'2004'), (2005, b'2005'), (2006, b'2006'), (2007, b'2007'), (2008, b'2008'), (2009, b'2009'), (2010, b'2010'), (2011, b'2011'), (2012, b'2012'), (2013, b'2013'), (2014, b'2014'), (2015, b'2015'), (2016, b'2016'), (2017, b'2017'), (0, b'Prefer not to disclose')]),
        ),
    ]
