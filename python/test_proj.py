from pyproj import Proj
# proj_param = "+proj=utm +ellps=WGS84 +lon_0=116 +lat_0=0.0n +x_0=0 +y_0=0 +units=m +k=1.0"
# p = Proj(proj_param)
# x,y = p(116,40)
# print("%.3f,%.3f"%(x,y))

from pyproj import CRS
from pyproj import Transformer

crs_4326 = CRS("WGS84")
# print(crs_4326)

crs_proj = CRS("EPSG:28992")

crs_4326 = CRS.from_epsg(4326)
crs_proj = CRS.from_epsg(26917)

transformer = Transformer.from_crs(crs_4326, crs_proj)
transformer.transform(52.067567, 5.068913)

# print(transformer)

# Proj('epsg:28992')(5.068913, 52.067567)

# from pyproj import CRS
# crs = CRS.from_epsg(4326)
# print(crs)

# crs = CRS.from_string("epsg:4326")
# print(crs)
# crs = CRS.from_proj4("+proj=latlon")
# print(crs)
# crs = CRS.from_user_input(4326)
# print(crs)

# crs = CRS.from_proj4("+proj=omerc +lat_0=-36 +lonc=147 +alpha=-54 +k=1 +x_0=0 +y_0=0 +gamma=0 +ellps=WGS84 +towgs84=0,0,0,0,0,0,0")
# print(crs)
# print(crs.to_wkt(pretty=True))

# from pyproj.enums import WktVersion
# print(crs.to_wkt(WktVersion.WKT1_GDAL, pretty=True))

# from pyproj import CRS
# from pyproj.aoi import AreaOfInterest
# from pyproj.database import query_utm_crs_info

# utm_crs_list = query_utm_crs_info(
#     datum_name="WGS 84",
#     area_of_interest=AreaOfInterest(
#         west_lon_degree=-93.581543,
#         south_lat_degree=42.032974,
#         east_lon_degree=-93.581543,
#         north_lat_degree=42.032974,
#     ),
# )
# utm_crs = CRS.from_epsg(utm_crs_list[0].code)
# print(utm_crs)

# crs_4326 = CRS.from_epsg(4326)
# crs_26917 = CRS.from_epsg(26917)

# from pyproj import Transformer
# transformer = Transformer.from_crs(crs_4326, crs_26917)
# transformer = Transformer.from_crs(4326, 26917)
# transformer = Transformer.from_crs("EPSG:4326", "EPSG:26917")

# print(transformer)

# from pyproj import Transformer
# transformer = Transformer.from_crs("EPSG:4326", "EPSG:26917", always_xy=True)
# transformer.transform(-80, 50)
# print(transformer.transform(-80, 50))

# from pyproj import Geod
# lats = [-72.9, -71.9, -74.9, -74.3, -77.5, -77.4, -71.7, -65.9, -65.7,
#         -66.6, -66.9, -69.8, -70.0, -71.0, -77.3, -77.9, -74.7]
# lons = [-74, -102, -102, -131, -163, 163, 172, 140, 113,
#         88, 59, 25, -4, -14, -33, -46, -61]
# geod = Geod(ellps="WGS84")
# total_length = geod.line_length(lons, lats)
# f"{total_length:.3f}"
# print(total_length)

# from pyproj import Geod
# lats = [-72.9, -71.9, -74.9, -74.3, -77.5, -77.4, -71.7, -65.9, -65.7,
#         -66.6, -66.9, -69.8, -70.0, -71.0, -77.3, -77.9, -74.7]
# lons = [-74, -102, -102, -131, -163, 163, 172, 140, 113,
#         88, 59, 25, -4, -14, -33, -46, -61]
# geod = Geod(ellps="WGS84")
# total_length = geod.line_length(lons, lats)
# print(f"{total_length:.3f}")

# from pyproj import Geod
# geod = Geod('+a=6378137 +f=0.0033528106647475126')
# lats = [-72.9, -71.9, -74.9, -74.3, -77.5, -77.4, -71.7, -65.9, -65.7,
#         -66.6, -66.9, -69.8, -70.0, -71.0, -77.3, -77.9, -74.7]
# lons = [-74, -102, -102, -131, -163, 163, 172, 140, 113,
#         88, 59, 25, -4, -14, -33, -46, -61]
# poly_area, poly_perimeter = geod.polygon_area_perimeter(lons, lats)
# print(f"{poly_area:.3f} {poly_perimeter:.3f}")

# from pyproj import CRS
# crs_4326 = CRS.from_epsg(4326)
# crs_26917 = CRS.from_epsg(26917)
# print(crs_26917)

# from pyproj import Transformer
# transformer = Transformer.from_crs(crs_4326, crs_26917)
# transformer = Transformer.from_crs(4326, 26917)
# transformer = Transformer.from_crs("EPSG:4326", "EPSG:26917")
# print(transformer)

from pyproj import Proj
p = Proj(proj='utm',zone=10,ellps='WGS84', preserve_units=False)
x,y = p(-120.108, 34.36116666)
# lonlat to xy
print('x=%9.3f y=%11.3f' % (x,y))
# xy to lonlat
print('lon=%8.3f lat=%5.3f' % p(x,y,inverse=True))

lons = (-119.72,-118.40,-122.38)
lats = (36.77, 33.93, 37.62 )
x,y = p(lons, lats)
print('x: %9.3f %9.3f %9.3f' % x)
print('y: %9.3f %9.3f %9.3f' % y)

lons, lats = p(x, y, inverse=True) # inverse transform
print('lons: %8.3f %8.3f %8.3f' % lons)
print('lats: %8.3f %8.3f %8.3f' % lats)

p2 = Proj('+proj=utm +zone=10 +ellps=WGS84', preserve_units=False)
x,y = p2(-120.108, 34.36116666)
print('x=%9.3f y=%11.3f' % (x,y))

p = Proj("epsg:32667", preserve_units=False)
print('x=%12.3f y=%12.3f (meters)' % p(-114.057222, 51.045))