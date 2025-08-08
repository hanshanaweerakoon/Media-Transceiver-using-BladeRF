# Design Notes – GNU Radio File Transfer (EN2130)

## 1. Overview
This project implements a *point-to-point digital wireless communication system* using GNU Radio and BladeRF SDR hardware.  
The primary goal is to transmit and receive arbitrary files (currently images) by embedding them in .tmp containers with headers and footers.

---

## 2. System Architecture

### 2.1 Transmitter
- Reads the original file from disk.
- Adds a *unique header* and *footer* to mark boundaries.
- Converts to .tmp format.
- Modulates data using *QPSK*.
- Sends via BladeRF at *2.42 GHz*.

### 2.2 Receiver
- Receives .tmp file over RF.
- Detects header/footer to extract payload.
- Writes the recovered file to disk.

---

## 3. Hardware & Software

### Hardware
- *BladeRF SDR* (driver=bladerf)
- Host PC

### Software
- *GNU Radio 3.10*
- *Python 3*
- PyQt5 for UI
- SoapySDR interface

---

## 4. Key Parameters

| Parameter          | Value          |
|--------------------|---------------|
| Modulation         | QPSK          |
| Samples/Symbol     | 4             |
| FEC                | Convolutional |
| Frequency          | 2.42 GHz      |
| Bandwidth          | 25 kHz        |
| MTU                | 1500 bytes    |

---

## 5. Design Choices

- *QPSK Modulation*: Balanced between bandwidth efficiency and noise resilience.
- *Convolutional Coding*: Improves BER in noisy channels.
- *Header/Footer Markers*: Simple approach for file framing without complex protocols.

---

## 6. Future Improvements

- Add *voice* and *video* transmission.
- Implement *security/encryption*.
- Add *channel estimation* and *adaptive modulation*.
- Optimize for *lower latency*.
-
