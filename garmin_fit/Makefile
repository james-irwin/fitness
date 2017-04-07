LIBSOURCES = \
../../../fit.cpp \
../../../fit_accumulated_field.cpp \
../../../fit_accumulator.cpp \
../../../fit_buffer_encode.cpp \
../../../fit_buffered_mesg_broadcaster.cpp \
../../../fit_buffered_record_mesg_broadcaster.cpp \
../../../fit_crc.cpp \
../../../fit_date_time.cpp \
../../../fit_decode.cpp \
../../../fit_developer_field.cpp \
../../../fit_developer_field_definition.cpp \
../../../fit_developer_field_description.cpp \
../../../fit_encode.cpp \
../../../fit_factory.cpp \
../../../fit_field.cpp \
../../../fit_field_base.cpp \
../../../fit_field_definition.cpp \
../../../fit_mesg.cpp \
../../../fit_mesg_broadcaster.cpp \
../../../fit_mesg_definition.cpp \
../../../fit_mesg_with_event_broadcaster.cpp \
../../../fit_profile.cpp \
../../../fit_protocol_validator.cpp \
../../../fit_unicode.cpp

CC=clang++
CFLAGS="--std=c++1y"

all: decode

fitlib.a: $(LIBSOURCES)
	$(CC) -c $(CFLAGS) $(LIBSOURCES) -I../../../
	ar -r fitlib.a *.o
	rm *.o
	ranlib fitlib.a

decode: fitlib.a decode.cpp
	$(CC) $(CFLAGS) -o decode decode.cpp fitlib.a -I../../../ 
