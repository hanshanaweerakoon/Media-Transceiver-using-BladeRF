# Media Transceiver using BladeRF – EN2130 Communication Design Project

This project was developed as project of the *EN2130 – Communication Design Project*. It demonstrates a *point-to-point digital wireless communication system* using *BladeRF* to transmit and receive arbitrary files. Currently implemented for *File transmission* over the *2.4 GHz ISM band* using BladeRF hardware and GNU Radio.

---

## 🎯 Project Requirements (From EN2130 Specification)

- Implement a point-to-point *digital wireless communication* system using SDRs.
- Support transmission of:
  - Images ✅ 
  - Voice ✅ 
  - Video ✅ 
- Operate in *2.4 GHz ISM band* within legal power limits.
- Include a *user interface* for operation.
- Performance evaluation:
  - With distance
  - End-to-end delay
- Optional features (future work):
  - Security
  - Channel estimation
  - Adaptive transmission

---

## 📂 Files

- Transmitter.py – Transmitter script  
  Converts a file to .tmp format with a header/footer, then transmits using QPSK modulation over SDR.

- Receiver.py – Receiver script  
  Receives .tmp file, detects the header/footer, and reconstructs the original file.

---

## 🛠 Requirements

- [GNU Radio 3.10+](https://www.gnuradio.org/)
- [BladeRF drivers](https://www.nuand.com/)
- Python 3
- PyQt5

Install dependencies (example for Ubuntu):
```bash
sudo apt update
sudo apt install gnuradio python3-pyqt5

