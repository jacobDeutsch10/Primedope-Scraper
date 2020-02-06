import Scraper

foo = Scraper.Scraper(wr_bb_100=10, wr_observed=10, std_dev=140, hands=151)
#foo.scrape_page_x_times(500, file_name="rawdatafrom500scrapes.csv")
#print(foo.average_with_rake_exclude_first_x_cols(rake=3, cols=8))
#foo.sort_data_by_plus_minus(file_name="plus_minus_500_scrapes.csv")
foo.read_raw_file_from_csv("rawdatafrom500scrapes.csv")
#foo.sort_data_by_plus_minus(file_name="plus_minus_500.csv")
print(foo.average_with_rake_exclude_first_x_cols())
#print(foo.get_avg_of_plus_minus(two_col_array=foo.read_plus_minus_file_from_csv("plus_minus_1k_no_bw.csv")))
