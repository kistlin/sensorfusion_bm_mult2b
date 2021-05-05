INCLUDE(CMakeForceCompiler)

SET(CMAKE_SYSTEM_NAME Generic)
SET(CMAKE_SYSTEM_PROCESSOR arm)
#SET(CMAKE_SYSTEM_VERSION 1)
#SET(CMAKE_CROSSCOMPILING TRUE)

if(APPLE)
	SET(COMPILER_POSTFIX )
	SET(TOOLCHAIN_DIR "/Applications/MCUXpressoIDE_11.3.0_5222/ide/plugins/com.nxp.mcuxpresso.tools.macosx_11.3.0.202011031536/tools/bin/")
elseif(UNIX)
	SET(COMPILER_POSTFIX )
	#SET(CMAKE_MAKE_PROGRAM /usr/bin/make)
	SET(TOOLCHAIN_DIR "/usr/local/mcuxpresso-ide/ide/tools/bin/")
else()
	SET(COMPILER_POSTFIX .exe)
	SET(CMAKE_MAKE_PROGRAM "C:/nxp/MCUXpressoIDE_11.1.1_3241/ide/buildtools/bin/make.exe")
	SET(TOOLCHAIN_DIR "C:/nxp/MCUXpressoIDE_11.1.1_3241/ide/tools/bin/")
endif(APPLE)

SET(CROSS_COMPILER_PREFIX arm-none-eabi-)

#SET(CMAKE_ASM_COMPILER ${TOOLCHAIN_DIR}${CROSS_COMPILER_PREFIX}gcc${COMPILER_POSTFIX})
SET(CMAKE_C_COMPILER   ${TOOLCHAIN_DIR}${CROSS_COMPILER_PREFIX}gcc${COMPILER_POSTFIX})
SET(CMAKE_CXX_COMPILER ${TOOLCHAIN_DIR}${CROSS_COMPILER_PREFIX}g++${COMPILER_POSTFIX})
SET(CMAKE_LINKER       ${TOOLCHAIN_DIR}${CROSS_COMPILER_PREFIX}ld${COMPILER_POSTFIX})
#SET(CMAKE_AR           ${TOOLCHAIN_DIR}${CROSS_COMPILER_PREFIX}ar${COMPILER_POSTFIX})
SET(CMAKE_OBJCOPY      ${TOOLCHAIN_DIR}${CROSS_COMPILER_PREFIX}objcopy${COMPILER_POSTFIX})
SET(CMAKE_OBJDUMP      ${TOOLCHAIN_DIR}${CROSS_COMPILER_PREFIX}objdump${COMPILER_POSTFIX})
SET(CMAKE_SIZE         ${TOOLCHAIN_DIR}${CROSS_COMPILER_PREFIX}size${COMPILER_POSTFIX})

# CLion refused to generate valid files without this (could not compile ...)
set(CMAKE_C_COMPILER_ID       GNU)
set(CMAKE_CXX_COMPILER_ID     GNU)
set(CMAKE_C_COMPILER_FORCED   TRUE)
set(CMAKE_CXX_COMPILER_FORCED TRUE)

# search for programs in the build host directories
SET(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)  # linker error because of startup code
# for libraries and headers in the target directories
SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)

# # CPU relevant flags
# # placed here so that all libraries and projects use the same CPU architecture
# # else for example there is problems because the arm instruction set is used by
# # default, which leads to compile errors when compiling assembly
# set(CMAKE_COMMON_FLAGS "${CMAKE_COMMON_FLAGS} -mlittle-endian")
# set(CMAKE_COMMON_FLAGS "${CMAKE_COMMON_FLAGS} -mcpu=cortex-m4")
# set(CMAKE_COMMON_FLAGS "${CMAKE_COMMON_FLAGS} -march=armv7e-m")
# set(CMAKE_COMMON_FLAGS "${CMAKE_COMMON_FLAGS} -mfloat-abi=hard")
# set(CMAKE_COMMON_FLAGS "${CMAKE_COMMON_FLAGS} -mfpu=fpv4-sp-d16")
# set(CMAKE_COMMON_FLAGS "${CMAKE_COMMON_FLAGS} -mthumb")
#
# # cache the flags for use
# #MESSAGE(STATUS "FLAGS: " ${CMAKE_COMMON_FLAGS} )
# set(CMAKE_C_FLAGS   "${CMAKE_COMMON_FLAGS}" CACHE STRING "CFLAGS")
# set(CMAKE_CXX_FLAGS "${CMAKE_COMMON_FLAGS}" CACHE STRING "CXXFLAGS")
# set(CMAKE_ASM_FLAGS "${CMAKE_COMMON_FLAGS}" CACHE STRING "")
