-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Des 2022 pada 13.01
-- Versi server: 10.1.34-MariaDB
-- Versi PHP: 7.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sepatu`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `barang_keluar`
--

CREATE TABLE `barang_keluar` (
  `id` int(11) NOT NULL,
  `id_sepatu` int(11) NOT NULL,
  `jumlah` int(11) NOT NULL DEFAULT '0',
  `stok_sebelum` int(11) NOT NULL DEFAULT '0',
  `stok_sesudah` int(11) NOT NULL DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `barang_keluar`
--

INSERT INTO `barang_keluar` (`id`, `id_sepatu`, `jumlah`, `stok_sebelum`, `stok_sesudah`, `created_at`, `updated_at`) VALUES
(1, 1, 3, 13, 10, '2022-11-27 03:08:43', '2022-11-27 03:08:43'),
(2, 1, 10, 14, 4, '2022-12-10 15:25:37', '2022-12-10 15:25:37'),
(3, 1, 2, 4, 2, '2022-12-10 15:30:08', '2022-12-10 15:30:08'),
(4, 1, 5, 7, 2, '2022-12-11 14:49:13', '2022-12-11 14:49:13'),
(5, 1, 5, 31, 26, '2022-12-12 18:25:24', '2022-12-12 18:25:24');

-- --------------------------------------------------------

--
-- Struktur dari tabel `barang_masuk`
--

CREATE TABLE `barang_masuk` (
  `id` int(11) NOT NULL,
  `id_sepatu` int(11) NOT NULL,
  `jumlah` int(11) NOT NULL DEFAULT '0',
  `stok_sebelum` int(11) NOT NULL DEFAULT '0',
  `stok_sesudah` int(11) NOT NULL DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `barang_masuk`
--

INSERT INTO `barang_masuk` (`id`, `id_sepatu`, `jumlah`, `stok_sebelum`, `stok_sesudah`, `created_at`, `updated_at`) VALUES
(1, 1, 3, 10, 13, '2022-11-27 03:07:22', '2022-11-27 03:08:26'),
(4, 1, 5, 10, 15, '2022-12-10 14:44:59', '2022-12-10 14:44:59'),
(5, 1, 4, 10, 14, '2022-12-10 14:47:36', '2022-12-10 14:47:36'),
(6, 3, 6, 0, 6, '2022-12-10 14:49:24', '2022-12-10 14:49:24'),
(18, 1, 13, 18, 31, '2022-12-12 18:22:07', '2022-12-12 18:22:07');

-- --------------------------------------------------------

--
-- Struktur dari tabel `merk`
--

CREATE TABLE `merk` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `merk`
--

INSERT INTO `merk` (`id`, `nama`) VALUES
(1, 'Ventela'),
(2, 'Aerostreet'),
(3, 'Compass'),
(4, 'Geoff Max'),
(5, 'Piero');

-- --------------------------------------------------------

--
-- Struktur dari tabel `sepatu`
--

CREATE TABLE `sepatu` (
  `id` int(11) NOT NULL,
  `id_series` int(11) NOT NULL,
  `ukuran` int(11) NOT NULL,
  `stok` int(11) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `sepatu`
--

INSERT INTO `sepatu` (`id`, `id_series`, `ukuran`, `stok`, `created_at`, `updated_at`) VALUES
(1, 1, 40, 26, '2022-11-16 20:04:58', '2022-12-12 18:25:24'),
(2, 1, 41, 7, '2022-11-16 20:04:58', '2022-12-08 13:59:15'),
(3, 1, 42, 20, '2022-12-10 14:49:24', '2022-12-10 15:10:10'),
(4, 2, 40, 14, '2022-12-10 15:12:12', '2022-12-10 15:12:29'),
(5, 1, 43, 10, '2022-12-11 14:46:05', '2022-12-11 14:46:05'),
(6, 16, 40, 10, '2022-12-12 13:47:24', '2022-12-12 13:47:24');

-- --------------------------------------------------------

--
-- Struktur dari tabel `series`
--

CREATE TABLE `series` (
  `id` int(11) NOT NULL,
  `id_merk` int(11) NOT NULL,
  `kode` varchar(50) DEFAULT NULL,
  `nama` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `series`
--

INSERT INTO `series` (`id`, `id_merk`, `kode`, `nama`) VALUES
(1, 1, 'S001', 'Republic Low White'),
(2, 1, 'S002', 'Casual Basic'),
(3, 1, 'S003', 'Basic Black Natural Low'),
(4, 1, 'S004', 'Ethnic High Black Nature'),
(5, 1, 'S005', 'Ventela x Evil x Papa Gading'),
(6, 2, 'S006', 'Massive White Gum'),
(7, 2, 'S007', 'Arrow White'),
(8, 2, 'S008', 'Jhoose Black'),
(9, 2, 'S009', 'Hoops High All Black'),
(10, 2, 'S010', 'Massive All Black'),
(11, 3, 'S011', 'Compass x Boy Pablo'),
(12, 3, 'S012', 'Gazelle Low Black'),
(13, 3, 'S013', 'Velocity'),
(14, 3, 'S014', 'RetroGrade Black White'),
(15, 3, 'S015', 'Red Gum'),
(16, 4, 'S016', 'Ethan Black'),
(17, 4, 'S017', 'Timeless Low Black'),
(18, 4, 'S018', 'Authentic Black Gum'),
(19, 4, 'S019', 'Meery All Black'),
(20, 4, 'S020', 'Larryflow Black White'),
(21, 5, 'S021', 'Jorge Black'),
(22, 5, 'S022', 'Rawedge White'),
(23, 5, 'S023', 'Ergo Street Dark'),
(24, 5, 'S024', 'Reno Navy'),
(25, 5, 'S025', 'Arcwave Red Black');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `created_at`, `updated_at`) VALUES
(1, 'admin', '21232f297a57a5a743894a0e4a801fc3', '2022-11-16 01:44:04', '2022-11-16 01:44:19');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `barang_keluar`
--
ALTER TABLE `barang_keluar`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `barang_masuk`
--
ALTER TABLE `barang_masuk`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `merk`
--
ALTER TABLE `merk`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `sepatu`
--
ALTER TABLE `sepatu`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `series`
--
ALTER TABLE `series`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `barang_keluar`
--
ALTER TABLE `barang_keluar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `barang_masuk`
--
ALTER TABLE `barang_masuk`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT untuk tabel `merk`
--
ALTER TABLE `merk`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `sepatu`
--
ALTER TABLE `sepatu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `series`
--
ALTER TABLE `series`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
