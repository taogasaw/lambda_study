# -*- coding: utf-8 -*-
import sys

#  station_identifier    :integer
#  name                  :string           default(""), not null
#  address               :string           default(""), not null
#  telephone             :string
#  company_name          :string           default(""), not null
#  description           :text
#  main_image_url        :string           default(""), not null
#  sub_image_url         :string           default(""), not null
#  comment               :text
#  start_at              :date
#  end_at                :date
#  express_start_at      :date
#  express_end_at        :date
#  special_note          :text
#  salary_min            :decimal(, )
#  salary_max            :decimal(, )
#  pattern               :string
#  term_name             :text
#  worktime              :text
#  treatment             :text
#  requirement           :text
#  category_names        :string
#  feature_names         :string
#  application_method    :text
#  company_info          :text
#  contact_name          :string           default(""), not null
#  contact_email         :string           default(""), not null
#  dropped               :boolean          default(TRUE), not null
#  entry_url             :string           default(""), not null
#  shop_identifier       :string           default(""), not null
#  allow_not_addressable :boolean          default(FALSE), not null
#  no_geocoding          :boolean          default(FALSE), not null
#  outside               :boolean          default(FALSE), not null


class CsvContainer(object):
    def __init__(self):
        self._station_identifier = None
        self._name = ''
        self._address = ''
        self._telephone = None
        self._company_name = ''
        self._description = None
        self._main_image_url = ''
        self._sub_image_url = ''
        self._comment = None
        self._start_at = None  # datetime.strptime('2000/1/1', '%Y/%m/%d')
        self._end_at = None  # datetime.strptime('2000/1/1', '%Y/%m/%d')
        self._express_start_at = None
        self._express_end_at = None
        self._special_note = None
        self._salary_min = None
        self._salary_max = None
        self._pattern = None
        self._term_name = None
        self._worktime = None
        self._treatment = None
        self._requirement = None
        self._category_names = None
        self._feature_names = None
        self._application_method = None
        self._company_info = None
        self._contact_name = ''
        self._contact_email = ''
        self._dropped = True
        self._entry_url = ''
        self._shop_identifier = ''
        self._allow_not_addressable = False
        self._no_geocoding = False
        self._outside = False

        reload(sys)
        sys.setdefaultencoding("utf-8")

    @property  # プロパティ ゲッター
    def station_identifier(self):  # 自分自身が一つ目の引数に入るらしい
        return self._station_identifier

    @station_identifier.setter  # セッター
    def station_identifier(self, val):
        self._station_identifier = str(val)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = str(val)

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, val):
        self._address = str(val)

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, val):
        self._telephone = val

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, val):
        self._company_name = str(val)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, val):
        self._description = val

    @property
    def main_image_url(self):
        return self._main_image_url

    @main_image_url.setter
    def main_image_url(self, val):
        self._main_image_url = str(val)

    @property
    def sub_image_url(self):
        return self._sub_image_url

    @sub_image_url.setter
    def sub_image_url(self, val):
        self._sub_image_url = str(val)

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, val):
        self._comment = val

    @property
    def start_at(self):
        return self._start_at

    @start_at.setter
    def start_at(self, val):
        self._start_at = val

    @property
    def end_at(self):
        return self._end_at

    @end_at.setter
    def end_at(self, val):
        self._end_at = val

    @property
    def express_start_at(self):
        return self._express_start_at

    @express_start_at.setter
    def express_start_at(self, val):
        self._express_start_at = val

    @property
    def express_end_at(self):
        return self._express_end_at

    @express_end_at.setter
    def express_end_at(self, val):
        self._express_end_at = val

    @property
    def special_note(self):
        return self._special_note

    @special_note.setter
    def special_note(self, val):
        self._special_note = val

    @property
    def salary_min(self):
        return self._salary_min

    @salary_min.setter
    def salary_min(self, val):
        self._salary_min = val

    @property
    def salary_max(self):
        return self._salary_max

    @salary_max.setter
    def salary_max(self, val):
        self._salary_max = val

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, val):
        self._pattern = val

    @property
    def term_name(self):
        return self._term_name

    @term_name.setter
    def term_name(self, val):
        self._term_name = val

    @property
    def worktime(self):
        return self._worktime

    @worktime.setter
    def worktime(self, val):
        self._worktime = val

    @property
    def treatment(self):
        return self._treatment

    @treatment.setter
    def treatment(self, val):
        self._treatment = val

    @property
    def requirement(self):
        return self._requirement

    @requirement.setter
    def requirement(self, val):
        self._requirement = val

    @property
    def category_names(self):
        return self._category_names

    @category_names.setter
    def category_names(self, val):
        self._category_names = val

    @property
    def feature_names(self):
        return self._feature_names

    @feature_names.setter
    def feature_names(self, val):
        self._feature_names = val

    @property
    def application_method(self):
        return self._application_method

    @application_method.setter
    def application_method(self, val):
        self._application_method = val

    @property
    def company_info(self):
        return self._company_info

    @company_info.setter
    def company_info(self, val):
        self._company_info = val

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, val):
        self._contact_name = str(val)

    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, val):
        self._contact_email = str(val)

    @property
    def dropped(self):
        return self._dropped

    @dropped.setter
    def dropped(self, val):
        self._dropped = bool(val)

    @property
    def entry_url(self):
        return self._entry_url

    @entry_url.setter
    def entry_url(self, val):
        self._entry_url = str(val)

    @property
    def shop_identifier(self):
        return self._shop_identifier

    @shop_identifier.setter
    def shop_identifier(self, val):
        self._shop_identifier = str(val)

    @property
    def allow_not_addressable(self):
        return self._allow_not_addressable

    @allow_not_addressable.setter
    def allow_not_addressable(self, val):
        self._allow_not_addressable = bool(val)

    @property
    def no_geocoding(self):
        return self._no_geocoding

    @no_geocoding.setter
    def no_geocoding(self, val):
        self._no_geocoding = bool(val)

    @property
    def outside(self):
        return self._outside

    @outside.setter
    def outside(self, val):
        self._outside = bool(val)
