project(sensorfusion_bm_mult2b)
SET(ELF_FILE ${PROJECT_NAME}.elf)
INCLUDE(CMakeForceCompiler)

# CROSS COMPILER SETTING
SET(CMAKE_SYSTEM_NAME Generic)
CMAKE_MINIMUM_REQUIRED (VERSION 2.6)
ENABLE_LANGUAGE(C)
ENABLE_LANGUAGE(ASM)

# THE VERSION NUMBER
SET (Tutorial_VERSION_MAJOR 1)
SET (Tutorial_VERSION_MINOR 0)

# ENABLE ASM
#ENABLE_LANGUAGE(ASM)

SET(CMAKE_STATIC_LIBRARY_PREFIX)
SET(CMAKE_STATIC_LIBRARY_SUFFIX)

SET(CMAKE_EXECUTABLE_LIBRARY_PREFIX)
SET(CMAKE_EXECUTABLE_LIBRARY_SUFFIX)

 
# CURRENT DIRECTORY
SET(ProjDirPath ${CMAKE_CURRENT_SOURCE_DIR})


SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -DDEBUG")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -D__STARTUP_CLEAR_BSS")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -g")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -mcpu=cortex-m4")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -Wall")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -mfloat-abi=hard")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -mfpu=fpv4-sp-d16")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -mthumb")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -fno-common")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -ffunction-sections")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -fdata-sections")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -ffreestanding")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -fno-builtin")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -mapcs")
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -std=gnu99")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -DNDEBUG")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -D__STARTUP_CLEAR_BSS")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -mcpu=cortex-m4")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -Wall")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -mfloat-abi=hard")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -mfpu=fpv4-sp-d16")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -mthumb")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -fno-common")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -ffunction-sections")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -fdata-sections")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -ffreestanding")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -fno-builtin")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -mapcs")
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -std=gnu99")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DDEBUG")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DCPU_MK64FN1M0VLL12")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DFRDM_K64F")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DFREEDOM")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DPRINTF_ADVANCED_ENABLE")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DSERIAL_PORT_TYPE_UART=1")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -g")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -O0")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -mcpu=cortex-m4")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -Wall")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -mfloat-abi=hard")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -mfpu=fpv4-sp-d16")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -mthumb")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -MMD")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -MP")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -fno-common")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -ffunction-sections")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -fdata-sections")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -ffreestanding")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -fno-builtin")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -mapcs")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -std=gnu99")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -DNDEBUG")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -DCPU_MK64FN1M0VLL12")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -DFRDM_K64F")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -DFREEDOM")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -DPRINTF_ADVANCED_ENABLE")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -DSERIAL_PORT_TYPE_UART=1")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -Os")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -mcpu=cortex-m4")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -Wall")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -mfloat-abi=hard")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -mfpu=fpv4-sp-d16")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -mthumb")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -MMD")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -MP")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -fno-common")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -ffunction-sections")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -fdata-sections")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -ffreestanding")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -fno-builtin")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -mapcs")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -std=gnu99")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DCPU_MK64FN1M0VLL12")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DSERIAL_PORT_TYPE_UART=1")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -O0")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -mcpu=cortex-m4")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -mfloat-abi=hard")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -mfpu=fpv4-sp-d16")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -mthumb")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -MMD")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -MP")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fno-common")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -ffunction-sections")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fdata-sections")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -ffreestanding")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fno-builtin")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -mapcs")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fno-rtti")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fno-exceptions")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -DNDEBUG")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -DCPU_MK64FN1M0VLL12")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -DSERIAL_PORT_TYPE_UART=1")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Os")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -mcpu=cortex-m4")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Wall")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -mfloat-abi=hard")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -mfpu=fpv4-sp-d16")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -mthumb")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -MMD")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -MP")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -fno-common")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -ffunction-sections")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -fdata-sections")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -ffreestanding")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -fno-builtin")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -mapcs")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -fno-rtti")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -fno-exceptions")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -g")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -mcpu=cortex-m4")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -Wall")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -mfloat-abi=hard")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -mfpu=fpv4-sp-d16")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} --specs=nano.specs")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} --specs=nosys.specs")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -fno-common")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -ffunction-sections")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -fdata-sections")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -ffreestanding")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -fno-builtin")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -mthumb")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -mapcs")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -Xlinker")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} --gc-sections")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -Xlinker")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -static")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -Xlinker")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -z")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -Xlinker")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} muldefs")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -Xlinker")
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -Map=output.map")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -mcpu=cortex-m4")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -Wall")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -mfloat-abi=hard")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -mfpu=fpv4-sp-d16")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} --specs=nano.specs")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} --specs=nosys.specs")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -fno-common")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -ffunction-sections")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -fdata-sections")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -ffreestanding")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -fno-builtin")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -mthumb")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -mapcs")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -Xlinker")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} --gc-sections")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -Xlinker")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -static")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -Xlinker")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -z")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -Xlinker")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} muldefs")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -Xlinker")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -Map=output.map")

#include_directories(${ProjDirPath}/..)
include_directories(${ProjDirPath}/source)
include_directories(${ProjDirPath}/startup)
include_directories(${ProjDirPath}/component/uart)
include_directories(${ProjDirPath}/sensor_fusion)
include_directories(${ProjDirPath}/component/lists)
include_directories(${ProjDirPath}/utilities)
include_directories(${ProjDirPath}/board)
include_directories(${ProjDirPath}/device)
include_directories(${ProjDirPath}/gpio_driver)
include_directories(${ProjDirPath}/CMSIS_driver)
include_directories(${ProjDirPath}/interfaces)
include_directories(${ProjDirPath}/CMSIS)
include_directories(${ProjDirPath}/component/serial_manager)
include_directories(${ProjDirPath}/drivers)
include_directories(${ProjDirPath}/sensors)

#include_directories(${ProjDirPath}/..)
#include_directories(${ProjDirPath}/../../../../..)
#include_directories(${ProjDirPath}/..)
#include_directories(${ProjDirPath}/../../../../../../../CMSIS/Include)
#include_directories(${ProjDirPath}/../../../../../../../devices)
#include_directories(${ProjDirPath}/../../../../../../../platform/drivers)
#include_directories(${ProjDirPath}/../../../../../../frdmk64f)
#include_directories(${ProjDirPath}/../../../../../../../devices/MK64F12/drivers)
#include_directories(${ProjDirPath}/../../../../../../../devices/MK64F12/cmsis_drivers)
#include_directories(${ProjDirPath}/../../../../../../../middleware/issdk/drivers/systick)
#include_directories(${ProjDirPath}/../../../../../../../middleware/issdk/drivers/gpio)
#include_directories(${ProjDirPath}/../../../../../../../middleware/issdk/drivers/gpio/kinetis)
#include_directories(${ProjDirPath}/../../../../../../../middleware/issdk/algorithms/sensorfusion/sources)
#include_directories(${ProjDirPath}/../../../../../../../middleware/issdk/sensors)
#include_directories(${ProjDirPath}/../../../../../../../devices/MK64F12/utilities/str)
#include_directories(${ProjDirPath}/../../../../../../../devices/MK64F12/utilities/debug_console)
#include_directories(${ProjDirPath}/../../../../../../../components/uart)
#include_directories(${ProjDirPath}/../../../../../../../components/serial_manager)
#include_directories(${ProjDirPath}/../../../../../../../components/lists)
#include_directories(${ProjDirPath}/../../../../../../../devices/MK64F12)
#include_directories(${ProjDirPath}/../../../../../../../CMSIS/Driver/Include)
#include_directories(${ProjDirPath}/../../../../../../../devices/MK64F12/utilities)

add_executable(${ELF_FILE}
"${ProjDirPath}/board/board.c"
"${ProjDirPath}/board/board.h"
"${ProjDirPath}/board/clock_config.c"
"${ProjDirPath}/board/clock_config.h"
"${ProjDirPath}/board/frdm_fxs_mult2b_shield.h"
"${ProjDirPath}/board/frdm_k64f.c"
"${ProjDirPath}/board/frdm_k64f.h"
"${ProjDirPath}/board/issdk_hal.h"
"${ProjDirPath}/board/pin_mux.c"
"${ProjDirPath}/board/pin_mux.h"
"${ProjDirPath}/board/RTE_Device.h"
"${ProjDirPath}/CMSIS/arm_common_tables.h"
"${ProjDirPath}/CMSIS/arm_const_structs.h"
"${ProjDirPath}/CMSIS/arm_math.h"
"${ProjDirPath}/CMSIS/cmsis_armcc.h"
"${ProjDirPath}/CMSIS/cmsis_armclang.h"
"${ProjDirPath}/CMSIS/cmsis_armclang_ltm.h"
"${ProjDirPath}/CMSIS/cmsis_compiler.h"
"${ProjDirPath}/CMSIS/cmsis_gcc.h"
"${ProjDirPath}/CMSIS/cmsis_iccarm.h"
"${ProjDirPath}/CMSIS/cmsis_version.h"
"${ProjDirPath}/CMSIS/core_cm4.h"
"${ProjDirPath}/CMSIS/mpu_armv7.h"
"${ProjDirPath}/CMSIS_driver/Driver_Common.h"
"${ProjDirPath}/CMSIS_driver/Driver_I2C.h"
"${ProjDirPath}/CMSIS_driver/Driver_SPI.h"
"${ProjDirPath}/CMSIS_driver/Driver_USART.h"
"${ProjDirPath}/component/lists/generic_list.c"
"${ProjDirPath}/component/lists/generic_list.h"
"${ProjDirPath}/component/serial_manager/serial_manager.c"
"${ProjDirPath}/component/serial_manager/serial_manager.h"
"${ProjDirPath}/component/serial_manager/serial_port_internal.h"
"${ProjDirPath}/component/serial_manager/serial_port_uart.c"
"${ProjDirPath}/component/serial_manager/serial_port_uart.h"
"${ProjDirPath}/component/uart/uart.h"
"${ProjDirPath}/component/uart/uart_adapter.c"
"${ProjDirPath}/device/fsl_device_registers.h"
"${ProjDirPath}/device/MK64F12.h"
"${ProjDirPath}/device/MK64F12_features.h"
"${ProjDirPath}/device/system_MK64F12.c"
"${ProjDirPath}/device/system_MK64F12.h"
"${ProjDirPath}/drivers/fsl_clock.c"
"${ProjDirPath}/drivers/fsl_clock.h"
"${ProjDirPath}/drivers/fsl_common.c"
"${ProjDirPath}/drivers/fsl_common.h"
"${ProjDirPath}/drivers/fsl_dmamux.c"
"${ProjDirPath}/drivers/fsl_dmamux.h"
"${ProjDirPath}/drivers/fsl_dspi.c"
"${ProjDirPath}/drivers/fsl_dspi.h"
"${ProjDirPath}/drivers/fsl_dspi_cmsis.c"
"${ProjDirPath}/drivers/fsl_dspi_cmsis.h"
"${ProjDirPath}/drivers/fsl_dspi_edma.c"
"${ProjDirPath}/drivers/fsl_dspi_edma.h"
"${ProjDirPath}/drivers/fsl_edma.c"
"${ProjDirPath}/drivers/fsl_edma.h"
"${ProjDirPath}/drivers/fsl_flash.h"
"${ProjDirPath}/drivers/fsl_ftfx_adapter.h"
"${ProjDirPath}/drivers/fsl_ftfx_cache.c"
"${ProjDirPath}/drivers/fsl_ftfx_cache.h"
"${ProjDirPath}/drivers/fsl_ftfx_controller.c"
"${ProjDirPath}/drivers/fsl_ftfx_controller.h"
"${ProjDirPath}/drivers/fsl_ftfx_features.h"
"${ProjDirPath}/drivers/fsl_ftfx_flash.c"
"${ProjDirPath}/drivers/fsl_ftfx_flash.h"
"${ProjDirPath}/drivers/fsl_ftfx_flexnvm.c"
"${ProjDirPath}/drivers/fsl_ftfx_flexnvm.h"
"${ProjDirPath}/drivers/fsl_ftfx_utilities.h"
"${ProjDirPath}/drivers/fsl_gpio.c"
"${ProjDirPath}/drivers/fsl_gpio.h"
"${ProjDirPath}/drivers/fsl_i2c.c"
"${ProjDirPath}/drivers/fsl_i2c.h"
"${ProjDirPath}/drivers/fsl_i2c_cmsis.c"
"${ProjDirPath}/drivers/fsl_i2c_cmsis.h"
"${ProjDirPath}/drivers/fsl_i2c_edma.c"
"${ProjDirPath}/drivers/fsl_i2c_edma.h"
"${ProjDirPath}/drivers/fsl_pit.c"
"${ProjDirPath}/drivers/fsl_pit.h"
"${ProjDirPath}/drivers/fsl_port.h"
"${ProjDirPath}/drivers/fsl_smc.c"
"${ProjDirPath}/drivers/fsl_smc.h"
"${ProjDirPath}/drivers/fsl_uart.c"
"${ProjDirPath}/drivers/fsl_uart.h"
"${ProjDirPath}/drivers/fsl_uart_cmsis.c"
"${ProjDirPath}/drivers/fsl_uart_cmsis.h"
"${ProjDirPath}/drivers/fsl_uart_edma.c"
"${ProjDirPath}/drivers/fsl_uart_edma.h"
"${ProjDirPath}/gpio_driver/Driver_GPIO.h"
"${ProjDirPath}/gpio_driver/gpio_driver.c"
"${ProjDirPath}/gpio_driver/gpio_driver.h"
"${ProjDirPath}/gpio_driver/gpio_driver_irq.c"
"${ProjDirPath}/interfaces/register_io_i2c.c"
"${ProjDirPath}/interfaces/register_io_i2c.h"
"${ProjDirPath}/interfaces/register_io_spi.c"
"${ProjDirPath}/interfaces/register_io_spi.h"
"${ProjDirPath}/interfaces/sensor_drv.h"
"${ProjDirPath}/interfaces/sensor_io_i2c.c"
"${ProjDirPath}/interfaces/sensor_io_i2c.h"
"${ProjDirPath}/interfaces/sensor_io_spi.c"
"${ProjDirPath}/interfaces/sensor_io_spi.h"
"${ProjDirPath}/MK64F12/gcc/MK64FN1M0xxx12_flash.ld"
"${ProjDirPath}/sensor_fusion/approximations.c"
"${ProjDirPath}/sensor_fusion/approximations.h"
"${ProjDirPath}/sensor_fusion/calibration_storage.c"
"${ProjDirPath}/sensor_fusion/calibration_storage.h"
"${ProjDirPath}/sensor_fusion/control.c"
"${ProjDirPath}/sensor_fusion/control.h"
"${ProjDirPath}/sensor_fusion/debug.c"
"${ProjDirPath}/sensor_fusion/debug.h"
"${ProjDirPath}/sensor_fusion/DecodeCommandBytes.c"
"${ProjDirPath}/sensor_fusion/driver_FXAS21002.c"
"${ProjDirPath}/sensor_fusion/driver_FXOS8700.c"
"${ProjDirPath}/sensor_fusion/driver_KSDK_NVM.c"
"${ProjDirPath}/sensor_fusion/driver_KSDK_NVM.h"
"${ProjDirPath}/sensor_fusion/driver_MPL3115.c"
"${ProjDirPath}/sensor_fusion/driver_pit.c"
"${ProjDirPath}/sensor_fusion/driver_pit.h"
"${ProjDirPath}/sensor_fusion/driver_systick.c"
"${ProjDirPath}/sensor_fusion/drivers.h"
"${ProjDirPath}/sensor_fusion/fusion.c"
"${ProjDirPath}/sensor_fusion/fusion.h"
"${ProjDirPath}/sensor_fusion/hal_frdm_fxs_mult2_b.c"
"${ProjDirPath}/sensor_fusion/magnetic.c"
"${ProjDirPath}/sensor_fusion/magnetic.h"
"${ProjDirPath}/sensor_fusion/matrix.c"
"${ProjDirPath}/sensor_fusion/matrix.h"
"${ProjDirPath}/sensor_fusion/orientation.c"
"${ProjDirPath}/sensor_fusion/orientation.h"
"${ProjDirPath}/sensor_fusion/output_stream.c"
"${ProjDirPath}/sensor_fusion/precisionAccelerometer.c"
"${ProjDirPath}/sensor_fusion/precisionAccelerometer.h"
"${ProjDirPath}/sensor_fusion/sensor_fusion.c"
"${ProjDirPath}/sensor_fusion/sensor_fusion.h"
"${ProjDirPath}/sensor_fusion/status.c"
"${ProjDirPath}/sensor_fusion/status.h"
"${ProjDirPath}/sensors/fxas21002.h"
"${ProjDirPath}/sensors/fxas21002_drv.c"
"${ProjDirPath}/sensors/fxas21002_drv.h"
"${ProjDirPath}/sensors/fxos8700.h"
"${ProjDirPath}/sensors/fxos8700_drv.c"
"${ProjDirPath}/sensors/fxos8700_drv.h"
"${ProjDirPath}/sensors/mpl3115.h"
"${ProjDirPath}/sensors/mpl3115_drv.c"
"${ProjDirPath}/sensors/mpl3115_drv.h"
"${ProjDirPath}/source/build.h"
"${ProjDirPath}/source/main_baremetal.c"
"${ProjDirPath}/startup/startup_MK64F12.S"
"${ProjDirPath}/utilities/fsl_assert.c"
"${ProjDirPath}/utilities/fsl_debug_console.c"
"${ProjDirPath}/utilities/fsl_debug_console.h"
"${ProjDirPath}/utilities/fsl_debug_console_conf.h"
"${ProjDirPath}/utilities/fsl_sbrk.c"
"${ProjDirPath}/utilities/fsl_str.c"
"${ProjDirPath}/utilities/fsl_str.h"
"${ProjDirPath}/utilities/systick_utils.c"
"${ProjDirPath}/utilities/systick_utils.h"
)


set(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -T${ProjDirPath}/MK64FN1M0xxx12_flash.ld -static")

set(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -T${ProjDirPath}/MK64FN1M0xxx12_flash.ld -static")

TARGET_LINK_LIBRARIES(${ELF_FILE} -Wl,--start-group)
target_link_libraries(${ELF_FILE} debug m)
target_link_libraries(${ELF_FILE} debug c)
target_link_libraries(${ELF_FILE} debug gcc)
target_link_libraries(${ELF_FILE} debug nosys)
target_link_libraries(${ELF_FILE} optimized m)
target_link_libraries(${ELF_FILE} optimized c)
target_link_libraries(${ELF_FILE} optimized gcc)
target_link_libraries(${ELF_FILE} optimized nosys)
TARGET_LINK_LIBRARIES(${ELF_FILE} -Wl,--end-group)

set(HEX_FILE ${PROJECT_NAME}.hex)
set(BIN_FILE ${PROJECT_NAME}.bin)
add_custom_command(TARGET ${ELF_FILE} POST_BUILD
        COMMENT "Building ${HEX_FILE}"
        COMMAND ${CMAKE_OBJCOPY} -Oihex $<TARGET_FILE:${ELF_FILE}> ${HEX_FILE}
        COMMENT "Building ${BIN_FILE}"
        COMMAND ${CMAKE_OBJCOPY} -Obinary $<TARGET_FILE:${ELF_FILE}> ${BIN_FILE})
add_custom_command(TARGET ${ELF_FILE} POST_BUILD
        COMMENT "Create listing of ${ELF_FILE}"
        COMMAND ${CMAKE_OBJDUMP} --source --all-headers --demangle --disassemble --line-numbers --wide $<TARGET_FILE:${ELF_FILE}> > "${PROJECT_NAME}.lst")
add_custom_command(TARGET ${ELF_FILE} POST_BUILD
        COMMENT "Printing size of ${ELF_FILE}"
        COMMAND ${CMAKE_SIZE} --format=berkeley --totals  $<TARGET_FILE:${ELF_FILE}>)
