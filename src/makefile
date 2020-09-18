CCL += gcc
CXXCL += g++

INCLUDES += `pkg-config --cflags sndfile`
INCLUDES += `pkg-config --cflags fftw3`
INCLUDES += `pkg-config --cflags portaudio-2.0`

CFLAGS += -Ofast
CXXFLAGS += -Ofast -std=c++11

LDFLAGS += `pkg-config --libs sndfile`
LDFLAGS += `pkg-config --libs fftw3`
LDFLAGS += `pkg-config --libs portaudio-2.0`
LDFLAGS += -lcairo

OBJS += spectrum.o window.o common.o
EXECOBJ1 += create_spectrogram.o

all: $(EXECOBJ1) $(EXECOBJ2) $(EXECOBJ3) $(OBJS)
	$(CCL) -o create_spectrogram $(EXECOBJ1) $(OBJS) $(LDFLAGS)

%.o: %.c
	$(CCL) -c -pipe $(CFLAGS) $(DEFINES) $(INCLUDES) $<

%.o: %.cpp
	$(CXXCL) -c -pipe $(CXXFLAGS) $(DEFINES) $(INCLUDES) $<

clean:
	rm *.o; rm create_spectrogram
