# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cdi_forms.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cdi_forms', '0011_backgroundinfo_born_on_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='English_WG',
            fields=[
                ('itemID', models.CharField(max_length=101, serialize=False, primary_key=True)),
                ('item', models.CharField(max_length=101)),
                ('item_type', models.CharField(max_length=101)),
                ('category', models.CharField(max_length=101)),
                ('choices', models.CharField(max_length=101)),
                ('uni_lemma', models.CharField(max_length=101, null=True, blank=True)),
                ('definition', models.CharField(max_length=201, null=True, blank=True)),
                ('gloss', models.CharField(max_length=1001, null=True, blank=True)),
                ('complexity_category', models.CharField(max_length=101, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='requests_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_hash', models.CharField(max_length=128)),
                ('request_type', models.CharField(max_length=4)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='birth_weight',
            field=models.FloatField(verbose_name=b'Birth weight (In pounds)', validators=[cdi_forms.models.validate_g_zero, django.core.validators.MaxValueValidator(14, b'Birth weight is not expected to be more than 14 pounds')]),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='caregiver_info',
            field=models.IntegerField(verbose_name=b'Does your child live with:', choices=[(2, b'Two parents'), (1, b'One parent'), (0, b'Other caregivers (e.g., grandparent or grandparents)')]),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='father_education',
            field=models.IntegerField(help_text=b'Choose highest grade completed (12 = high school graduate; 16 = college graduate; 18 = advanced degree)', verbose_name=b"Father's (or Parent 2) Education", choices=[(5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12 (High school graduate)'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16 (College graduate)'), (17, b'17'), (18, b'18 (Advanced degree)'), (19, b'19'), (20, b'20'), (21, b'21'), (22, b'22'), (23, b'23')]),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='father_yob',
            field=models.IntegerField(verbose_name=b"Father's (or Parent 2) Year of birth", choices=[(1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)]),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='mother_education',
            field=models.IntegerField(help_text=b'Choose highest grade completed (12 = high school graduate; 16 = college graduate; 18 = advanced degree)', verbose_name=b"Mother's (or Parent 1) Education", choices=[(5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12 (High school graduate)'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16 (College graduate)'), (17, b'17'), (18, b'18 (Advanced degree)'), (19, b'19'), (20, b'20'), (21, b'21'), (22, b'22'), (23, b'23')]),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='mother_yob',
            field=models.IntegerField(verbose_name=b"Mother's (or Parent 1) Year of birth", choices=[(1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)]),
        ),
        migrations.AlterField(
            model_name='english_ws',
            name='complexity_category',
            field=models.CharField(max_length=101, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='english_ws',
            name='definition',
            field=models.CharField(max_length=201, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='english_ws',
            name='gloss',
            field=models.CharField(max_length=101, null=True, blank=True),
        ),
    ]
