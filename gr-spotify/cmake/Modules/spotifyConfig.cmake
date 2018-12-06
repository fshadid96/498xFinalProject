INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SPOTIFY spotify)

FIND_PATH(
    SPOTIFY_INCLUDE_DIRS
    NAMES spotify/api.h
    HINTS $ENV{SPOTIFY_DIR}/include
        ${PC_SPOTIFY_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SPOTIFY_LIBRARIES
    NAMES gnuradio-spotify
    HINTS $ENV{SPOTIFY_DIR}/lib
        ${PC_SPOTIFY_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SPOTIFY DEFAULT_MSG SPOTIFY_LIBRARIES SPOTIFY_INCLUDE_DIRS)
MARK_AS_ADVANCED(SPOTIFY_LIBRARIES SPOTIFY_INCLUDE_DIRS)

