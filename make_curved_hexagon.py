import numpy as np


class Round_Hexagon:

    def __init__(self, rad):
        self.rad = rad

    def remove_yz1(self, sharpcorners):
        # Find center of the circle
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        entireh = -min(y)
        h = entireh - np.sqrt(3) * self.rad / 2 - self.rad / (2 * np.sqrt(3))
        yc = -h
        zc = 0
        # Find points where circle meets hexagon border
        y1 = int(yc - np.sqrt(3) * self.rad / 2)
        z1 = int(self.rad / 2)
        y2 = y1
        z2 = -z1
        # Define 'orange' points #
        idxp = np.where((y < y1)
                        & ((y - yc)**2 + (z - zc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [y1, z1, y2, z2]
        return rounded, tanpnts

    def remove_yz2(self, sharpcorners):
        # Find center of the circle
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        entireh = max(y)
        h = entireh - np.sqrt(3) * self.rad / 2 - self.rad / (2 * np.sqrt(3))
        yc = h
        zc = 0
        # Find points where circle meets hexagon border
        y1 = int(yc + np.sqrt(3) * self.rad / 2)
        z1 = int(self.rad / 2)
        y2 = y1
        z2 = -z1
        # Define 'orange' points #
        idxp = np.where((y > y1)
                        & ((y - yc)**2 + (z - zc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) ##
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [y1, z1, y2, z2]
        return rounded, tanpnts

    def remove_yz3(self, sharpcorners):
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        top = np.where(sharpcorners[:, 2] == max(sharpcorners[:, 2]))[0]
        # Center of circle
        entireh = -min(sharpcorners[top, 1]) * 2
        h = entireh - np.sqrt(3) * self.rad / 2 - self.rad / (2 * np.sqrt(3))
        yc = -h / 2
        zc = np.sqrt(3) * h / 2
        # Find points where circle meets hexagon border
        y1 = int(yc)
        z1 = int(zc + self.rad)
        y2 = int(y1 - np.sqrt(3) * self.rad / 2)
        z2 = int(zc + self.rad / 2)
        # Define 'orange' points #
        idxp = np.where((y < y1) & (z > z2)
                        & ((y - yc)**2 + (z - zc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [y1, z1, y2, z2]
        return rounded, tanpnts

    def remove_yz4(self, sharpcorners):
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        top = np.where(sharpcorners[:, 2] == max(sharpcorners[:, 2]))[0]
        # Center of circle
        entireh = max(sharpcorners[top, 1]) * 2
        h = entireh - np.sqrt(3) * self.rad / 2 - self.rad / (2 * np.sqrt(3))
        yc = h / 2
        zc = np.sqrt(3) * h / 2
        # Find points where circle meets hexagon border
        y1 = int(yc)
        z1 = int(zc + self.rad)
        y2 = int(y1 - np.sqrt(3) * self.rad / 2)
        z2 = int(zc + self.rad / 2)
        # Define 'orange' points #
        idxp = np.where((y > y1) & (z > z2)
                        & ((y - yc)**2 + (z - zc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [y1, z1, y2, z2]
        return rounded, tanpnts

    def remove_yz5(self, sharpcorners):
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        bot = np.where(sharpcorners[:, 2] == min(sharpcorners[:, 2]))[0]
        # Center of circle
        entireh = max(sharpcorners[bot, 1]) * 2
        h = entireh - np.sqrt(3) * self.rad / 2 - self.rad / (2 * np.sqrt(3))
        yc = h / 2
        zc = -np.sqrt(3) * h / 2
        # Find points where circle meets hexagon border
        y1 = int(yc)
        z1 = int(zc - self.rad)
        y2 = int(y1 + np.sqrt(3) * self.rad / 2)
        z2 = int(zc - self.rad / 2)
        # Define 'orange' points #
        idxp = np.where((y > y1) & (z < z2)
                        & ((y - yc)**2 + (z - zc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [y1, z1, y2, z2]
        return rounded, tanpnts

    def remove_yz6(self, sharpcorners):
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        bot = np.where(sharpcorners[:, 2] == min(sharpcorners[:, 2]))[0]
        # Center of circle
        entireh = -min(sharpcorners[bot, 1]) * 2
        h = entireh - np.sqrt(3) * self.rad / 2 - self.rad / (2 * np.sqrt(3))
        yc = -h / 2
        zc = -np.sqrt(3) * h / 2
        # Find points where circle meets hexagon border
        y1 = int(yc)
        z1 = int(zc - self.rad)
        y2 = int(y1 - np.sqrt(3) * self.rad / 2)
        z2 = int(zc - self.rad / 2)
        # Define 'orange' points #
        idxp = np.where((y < y1) & (z < z2)
                        & ((y - yc)**2 + (z - zc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [y1, z1, y2, z2]
        return rounded, tanpnts

    def remove_yx1(self, sharpcorners):
        # Find center of the circle
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        left = np.where(sharpcorners[:, 1] == min(sharpcorners[:, 1]))[0][0]
        top = np.where(sharpcorners[:, 0] == max(sharpcorners[:, 0]))[0][0]
        yc = sharpcorners[left, 1] + self.rad
        xc = sharpcorners[top, 0] - self.rad
        # Find points where circle meets hexagon border
        y1 = yc - self.rad
        x1 = xc
        y2 = yc
        x2 = x1 + self.rad
        # Define 'orange' points #
        idxp = np.where((x > x1) & (y < y2)
                        & ((x - xc)**2 + (y - yc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [y1, x1, y2, x2]
        return rounded, tanpnts

    def remove_yx2(self, sharpcorners):
        # Find center of the circle
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        right = np.where(sharpcorners[:, 1] == max(sharpcorners[:, 1]))[0][0]
        top = np.where(sharpcorners[:, 0] == max(sharpcorners[:, 0]))[0][0]
        yc = sharpcorners[right, 1] - self.rad
        xc = sharpcorners[top, 0] - self.rad
        # Find points where circle meets hexagon border
        y1 = yc + self.rad
        x1 = xc
        y2 = yc
        x2 = x1 + self.rad
        # Define 'orange' points #
        idxp = np.where((x > x1) & (y > y2)
                        & ((x - xc)**2 + (y - yc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [y1, x1, y2, x2]
        return rounded, tanpnts

    def remove_yx3(self, sharpcorners):
        # Find center of the circle
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        right = np.where(sharpcorners[:, 1] == max(sharpcorners[:, 1]))[0][0]
        bot = np.where(sharpcorners[:, 0] == min(sharpcorners[:, 0]))[0][0]
        yc = sharpcorners[right, 1] - self.rad
        xc = sharpcorners[bot, 0] + self.rad
        # Find points where circle meets hexagon border
        y1 = yc + self.rad
        x1 = xc
        y2 = yc
        x2 = x1 - self.rad
        # Define 'orange' points #
        idxp = np.where((x < x1) & (y > y2)
                        & ((x - xc)**2 + (y - yc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [y1, x1, y2, x2]
        return rounded, tanpnts

    def remove_yx4(self, sharpcorners):
        # Find center of the circle
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        right = np.where(sharpcorners[:, 1] == min(sharpcorners[:, 1]))[0][0]
        bot = np.where(sharpcorners[:, 0] == min(sharpcorners[:, 0]))[0][0]
        yc = sharpcorners[right, 1] + self.rad
        xc = sharpcorners[bot, 0] + self.rad
        # Find points where circle meets hexagon border
        y1 = yc - self.rad
        x1 = xc
        y2 = yc
        x2 = x1 - self.rad
        # Define 'orange' points #
        idxp = np.where((x < x1) & (y < y2)
                        & ((x - xc)**2 + (y - yc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [y1, x1, y2, x2]
        return rounded, tanpnts

    def remove_zx1(self, sharpcorners):
        # Find center of the circle
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        left = np.where(sharpcorners[:, 2] == min(sharpcorners[:, 2]))[0][0]
        top = np.where(sharpcorners[:, 0] == max(sharpcorners[:, 0]))[0][0]
        zc = sharpcorners[left, 2] + self.rad
        xc = sharpcorners[top, 0] - self.rad
        # Find points where circle meets hexagon border
        z1 = zc - self.rad
        x1 = xc
        z2 = zc
        x2 = x1 + self.rad
        # Define 'orange' points #
        idxp = np.where((x > x1) & (z < z2)
                        & ((x - xc)**2 + (z - zc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [z1, x1, z2, x2]
        return rounded, tanpnts

    def remove_zx2(self, sharpcorners):
        tanpnts = []
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        # Find center of the circle
        right = np.where(sharpcorners[:, 2] == max(sharpcorners[:, 2]))[0][0]
        top = np.where(sharpcorners[:, 0] == max(sharpcorners[:, 0]))[0][0]
        zc = sharpcorners[right, 2] - self.rad
        xc = sharpcorners[top, 0] - self.rad
        # Find points where circle meets hexagon border
        z1 = zc + self.rad
        x1 = xc
        z2 = zc
        x2 = x1 + self.rad
        # Define 'orange' points #
        idxp = np.where((x > x1) & (z > z2)
                        & ((x - xc)**2 + (z - zc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [z1, x1, z2, x2]
        return rounded, tanpnts

    def remove_zx3(self, sharpcorners):
        tanpnts = []
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        # Find center of the circle
        right = np.where(sharpcorners[:, 2] == max(sharpcorners[:, 2]))[0][0]
        bot = np.where(sharpcorners[:, 0] == min(sharpcorners[:, 0]))[0][0]
        zc = sharpcorners[right, 2] - self.rad
        xc = sharpcorners[bot, 0] + self.rad
        # Find points where circle meets hexagon border
        z1 = zc + self.rad
        x1 = xc
        z2 = zc
        x2 = x1 - self.rad
        # Define 'orange' points #
        idxp = np.where((x < x1) & (z > z2)
                        & ((x - xc)**2 + (z - zc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [z1, x1, z2, x2]
        return rounded, tanpnts

    def remove_zx4(self, sharpcorners):
        tanpnts = []
        x = sharpcorners[:, 0]
        y = sharpcorners[:, 1]
        z = sharpcorners[:, 2]
        ICOMP = sharpcorners[:, 3]
        # Find center of the circle
        right = np.where(sharpcorners[:, 2] == min(sharpcorners[:, 2]))[0][0]
        bot = np.where(sharpcorners[:, 0] == min(sharpcorners[:, 0]))[0][0]
        zc = sharpcorners[right, 2] + self.rad
        xc = sharpcorners[bot, 0] + self.rad
        # Find points where circle meets hexagon border
        z1 = zc - self.rad
        x1 = xc
        z2 = zc
        x2 = x1 - self.rad
        # Define 'orange' points #
        idxp = np.where((x < x1) & (z < z2)
                        & ((x - xc)**2 + (z - zc)**2 > self.rad**2))[0]
        # Delete the orange points from the blue points (newpnts) #
        pnts_orange = np.column_stack((x[idxp], y[idxp], z[idxp], ICOMP[idxp]))
        idx2remove = []
        for j in range(len(pnts_orange)):
            idx_remove = np.where((sharpcorners == pnts_orange[j, :]).all(axis=1))
            idx2remove.append(idx_remove[0][0])
        rounded = np.delete(sharpcorners, idx2remove, 0)
        tanpnts = [z1, x1, z2, x2]
        return rounded, tanpnts
