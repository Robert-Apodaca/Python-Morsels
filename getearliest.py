def get_earliest(firstdate, seconddate):
    """Geat earliest date of 2 passed"""
    firstdate_year = firstdate[6:]
    seconddate_year = seconddate[6:]
    if firstdate_year < seconddate_year:
        return firstdate
    if seconddate_year < firstdate_year:
        return seconddate
    firstdate_month = firstdate[:3]
    seconddate_month = seconddate[:3]
    if firstdate_month < seconddate_month:
        return firstdate
    if seconddate_month < firstdate_month:
        return seconddate
    if firstdate[3:5] < seconddate[3:5]:
        return firstdate
    if seconddate[3:5] < firstdate[3:5]:
        return seconddate
    # firstdate_day = firstdate[3:5]
    # seconddate_day = seconddate[3:5]
    # if firstdate_day

#def get_earliest(date1, date2):
#    """Return earliest of two MM/DD/YYYY-formatted date strings."""
#    m1, d1, y1 = date1.split('/')
 #   m2, d2, y2 = date2.split('/')
  #  if (y1, m1, d1) < (y2, m2, d2):  #or return date1 if (y1, m1, d1) < (y2, m2, d2) else date2
   #     return date1
    #else:
     #   return date2